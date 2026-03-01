"""
quality_gate.py — Checklist de Qualidade Pré-Publicação
=========================================================
Garante que nenhum vídeo abaixo do padrão mínimo seja publicado.

Checklist validado antes de qualquer upload:
  - Resolução mínima 1080x1920 (9:16 vertical)
  - Duração entre 15s e 90s
  - Áudio presente (não mudo)
  - Sem tela preta nos primeiros 0.5s (o "frame preto" fatal)
  - Metadados não-vazios (title, description, tags)
  - Título não genérico (não é "Vídeo Novo!" ou similar)

Score 0-100: 100 = perfeito, <60 = bloquear publicação.
"""

import os
import logging
from dataclasses import dataclass, field
from typing import List, Optional

logger = logging.getLogger("quality_gate")


# =============================================================================
# MODELOS
# =============================================================================

PLACEHOLDER_TITLES = {
    "vídeo novo!", "video novo!", "notícia do futebol",
    "noticia do futebol", "vídeo de futebol", "video de futebol",
    "novo vídeo", "novo video", "untitled", ""
}


@dataclass
class QualityReport:
    """Resultado do checklist de qualidade."""
    passed: bool = True
    score: int = 100          # 0-100
    issues: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    def fail(self, reason: str, penalty: int = 20):
        """Registra uma falha e aplica penalidade ao score."""
        self.passed = False
        self.issues.append(reason)
        self.score = max(0, self.score - penalty)

    def warn(self, reason: str, penalty: int = 5):
        """Registra um aviso (não bloqueia, só penaliza score)."""
        self.warnings.append(reason)
        self.score = max(0, self.score - penalty)

    def summary(self) -> str:
        status = "✅ APROVADO" if self.passed else "❌ REPROVADO"
        lines = [f"{status} | Score: {self.score}/100"]
        for issue in self.issues:
            lines.append(f"  ❌ {issue}")
        for warn in self.warnings:
            lines.append(f"  ⚠️  {warn}")
        return "\n".join(lines)


# =============================================================================
# CHECKLIST DE VÍDEO
# =============================================================================

def check_video_file(video_path: str, report: Optional[QualityReport] = None) -> QualityReport:
    """
    Valida o arquivo de vídeo gerado.

    Args:
        video_path: Caminho para o arquivo .mp4
        report: QualityReport existente (criado se None)

    Returns:
        QualityReport preenchido com status e score.
    """
    if report is None:
        report = QualityReport()

    if not video_path or not os.path.exists(video_path):
        report.fail("Arquivo de vídeo não encontrado", penalty=100)
        return report

    # Tamanho mínimo do arquivo (>100KB significa que não está vazio)
    size = os.path.getsize(video_path)
    if size < 100_000:
        report.fail(f"Arquivo muito pequeno ({size/1024:.0f}KB) — provavelmente corrompido", penalty=40)

    try:
        from moviepy.editor import VideoFileClip
        with VideoFileClip(video_path) as clip:

            # ── Duração ───────────────────────────────────────────────
            duration = clip.duration
            if duration < 15:
                report.fail(
                    f"Vídeo muito curto ({duration:.1f}s < 15s mínimo)",
                    penalty=30
                )
            elif duration > 90:
                report.warn(
                    f"Vídeo muito longo ({duration:.1f}s > 90s recomendado para Shorts)",
                    penalty=10
                )

            # ── Resolução ────────────────────────────────────────────
            w, h = clip.size
            if w != 1080 or h != 1920:
                report.warn(
                    f"Resolução {w}x{h} diferente do 1080x1920 padrão",
                    penalty=10
                )

            # ── Áudio ─────────────────────────────────────────────────
            if clip.audio is None:
                report.fail("Sem faixa de áudio no vídeo", penalty=30)
            else:
                try:
                    # Amostrar 0.5s de áudio para checar se não é mudo
                    audio_array = clip.audio.subclip(0, min(0.5, duration)).to_soundarray()
                    import numpy as np
                    rms = float(np.sqrt(np.mean(audio_array ** 2)))
                    if rms < 0.001:
                        report.fail("Áudio mudo ou inaudível (RMS < 0.001)", penalty=25)
                except Exception as e:
                    report.warn(f"Não foi possível verificar qualidade do áudio: {e}", penalty=5)

            # ── Tela preta no início ──────────────────────────────────
            try:
                # Captura o frame em t=0.1s e mede o brilho médio
                first_frame = clip.get_frame(0.1)
                import numpy as np
                mean_brightness = float(np.mean(first_frame))
                if mean_brightness < 5:
                    report.fail(
                        f"Tela preta detectada no início (brilho médio={mean_brightness:.1f})",
                        penalty=20
                    )
            except Exception as e:
                report.warn(f"Não foi possível verificar frame inicial: {e}", penalty=3)

            logger.info(
                "[QualityGate] Vídeo: %.1fs | %dx%d | %.1fMB | Score atual: %d",
                duration, w, h, size / 1e6, report.score
            )

    except Exception as e:
        report.fail(f"Falha crítica ao analisar o vídeo: {e}", penalty=50)

    return report


# =============================================================================
# CHECKLIST DE METADADOS
# =============================================================================

def check_metadata(
    title: str,
    description: str,
    tags: list,
    report: Optional[QualityReport] = None
) -> QualityReport:
    """
    Valida metadados (título, descrição, tags) antes do upload.

    Args:
        title: Título do vídeo
        description: Descrição do vídeo
        tags: Lista de hashtags/tags
        report: QualityReport existente (criado se None)
    """
    if report is None:
        report = QualityReport()

    # ── Título ────────────────────────────────────────────────────────
    if not title or title.strip().lower() in PLACEHOLDER_TITLES:
        report.fail(
            f"Título genérico ou vazio: '{title}' — não publicar assim",
            penalty=25
        )
    elif len(title) < 10:
        report.warn(
            f"Título muito curto ({len(title)} chars) — ideal >20 chars",
            penalty=5
        )
    elif len(title) > 100:
        report.warn(
            f"Título longo ({len(title)} chars) — YouTube exibe apenas 70 chars",
            penalty=3
        )

    # ── Descrição ─────────────────────────────────────────────────────
    if not description or len(description.strip()) < 30:
        report.fail(
            f"Descrição muito curta ({len(description)} chars) — prejudica SEO",
            penalty=15
        )
    elif description.strip().lower() in {"vídeo novo!", "video novo!", "confira as notícias."}:
        report.fail(
            "Descrição genérica — fallback de IA ativado, não publicar",
            penalty=20
        )

    # ── Tags ──────────────────────────────────────────────────────────
    if not tags or len(tags) < 5:
        report.warn(
            f"Poucas tags ({len(tags)}) — ideal ≥10 para SEO",
            penalty=8
        )

    # Tags mínimas obrigatórias para o canal
    mandatory = {"futebas", "futebol", "shorts"}
    existing_lower = {t.lower().lstrip("#") for t in tags}
    missing = mandatory - existing_lower
    if missing:
        report.warn(
            f"Tags obrigatórias ausentes: {missing}",
            penalty=5
        )

    logger.info(
        "[QualityGate] Metadados: title=%d chars | desc=%d chars | tags=%d | Score: %d",
        len(title), len(description), len(tags), report.score
    )

    return report


# =============================================================================
# GATE COMPLETO (vídeo + metadados)
# =============================================================================

def run_full_quality_gate(
    video_path: str,
    title: str,
    description: str,
    tags: list,
    min_score: int = 60
) -> QualityReport:
    """
    Executa o checklist completo de qualidade.

    Args:
        video_path: Caminho do .mp4 gerado
        title: Título do vídeo
        description: Descrição do vídeo
        tags: Lista de tags/hashtags
        min_score: Score mínimo para aprovação (padrão: 60)

    Returns:
        QualityReport com passed=True se score >= min_score.
    """
    report = QualityReport()

    # Roda os dois checklists usando o mesmo report
    check_video_file(video_path, report)
    check_metadata(title, description, tags, report)

    # Decisão final baseada no score mínimo
    if report.score < min_score:
        report.passed = False
        if not report.issues:
            report.issues.append(
                f"Score {report.score} abaixo do mínimo {min_score}"
            )

    logger.info("[QualityGate] %s", report.summary())
    return report
