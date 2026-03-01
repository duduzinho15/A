# =============================================================================
# app/services/fact_checker.py — Fact Guard: Validador Anti-Alucinação
# =============================================================================
# Ideia #21 — Valida roteiros gerados pela IA contra o texto-fonte original.
#
# 3 Camadas:
#   1. Regex Claims: Extrai placares e nomes, compara fonte vs roteiro
#   2. LLM Cross-Check: Usa Groq para listar discrepâncias factuais
#   3. Dicionário Anti-Typo: Fuzzy match contra termos corretos do futebol BR
# =============================================================================

import re
import logging
from typing import Optional
from difflib import SequenceMatcher

logger = logging.getLogger("fact_checker")


# =============================================================================
# DICIONÁRIO DE TERMOS CORRETOS (Camada 3)
# =============================================================================

FOOTBALL_TERMS = {
    # Apelidos de times
    "rubro-negro": ["rubbedo-negro", "rubro negro", "rubronegro", "rubbedo negro", "rublo-negro"],
    "alvinegro": ["alvi-negro", "alvenegro", "alvi negro"],
    "alviverde": ["alvi-verde", "alveverde", "alvi verde"],
    "tricolor": ["tri-color", "tri color"],
    "colorado": ["colourado", "collrado"],
    "auriverde": ["auri-verde", "auri verde"],
    # Estádios
    "Maracanã": ["Maracana", "maracana", "Marcanã"],
    "Neo Química Arena": ["Neo Quimica Arena", "Neo Quimica", "Neo Química"],
    "Allianz Parque": ["Alianz Parque", "Allianz Park", "Alianz Park"],
    "Arena MRV": ["Arena Mrv", "arena mrv"],
    "Morumbis": ["Morumbi", "Morumbís"],
    "Mineirão": ["Mineirao", "mineirao", "Minerão"],
    # Termos em inglês que não devem aparecer
    "CRISE": ["CRISIS", "Crisis"],
    "time": ["team"],
    "jogador": ["player"],
    "técnico": ["coach"],
    "campeonato": ["championship"],
    "gol": ["goal"],
}


# =============================================================================
# CAMADA 1: Extração de Claims (Regex)
# =============================================================================

def extract_scores(text: str) -> list[str]:
    """Extrai todos os placares do texto (ex: '3x2', '2 a 1', '3 a 2')."""
    patterns = [
        r'(\d+)\s*[xX×]\s*(\d+)',          # 3x2, 3X2, 3×2
        r'(\d+)\s+a\s+(\d+)',               # 3 a 2
        r'(\d+)\s*-\s*(\d+)',               # 3-2 (cuidado com datas)
    ]
    scores = []
    for pattern in patterns:
        matches = re.findall(pattern, text)
        for m in matches:
            scores.append(f"{m[0]}x{m[1]}")
    return scores


def extract_names(text: str) -> list[str]:
    """Extrai nomes próprios capitalizados (potenciais jogadores/times)."""
    # Palavras capitalizadas com 3+ chars, não no início de frase
    words = re.findall(r'(?<!\.\s)(?<!\n)\b([A-ZÁÉÍÓÚÂÊÔÀÃÕÇ][a-záéíóúâêôàãõç]{2,})\b', text)
    # Filtrar palavras comuns do português
    stop_words = {
        "Você", "Ele", "Ela", "Isso", "Mas", "Com", "Para", "Que", "Uma",
        "Não", "Mais", "Seu", "Sua", "Nos", "Das", "Dos", "Sem", "Por",
        "Está", "Como", "Sobre", "Após", "Outro", "Outros", "Ainda",
        "Também", "Então", "Pode", "Quer", "Vai", "Ter", "Ser", "Ver",
        "Siga", "Deixa", "Atenção", "Veja", "Olha", "Isso", "Esse",
        "Essa", "Este", "Esta", "Comente", "Siga"
    }
    return [w for w in words if w not in stop_words]


def compare_scores(source_scores: list[str], script_scores: list[str]) -> list[dict]:
    """Compara placares extraídos da fonte vs roteiro."""
    issues = []
    if not source_scores and script_scores:
        # Roteiro inventou um placar que não existe na fonte
        issues.append({
            "type": "invented_score",
            "detail": f"Roteiro menciona placar(es) {script_scores} mas a fonte não contém placares.",
            "severity": "high"
        })
    elif source_scores and script_scores:
        for ss in script_scores:
            if ss not in source_scores:
                # Placar do roteiro não bate com nenhum da fonte
                issues.append({
                    "type": "wrong_score",
                    "detail": f"Roteiro diz '{ss}' mas a fonte contém {source_scores}.",
                    "correction": source_scores[0] if source_scores else None,
                    "severity": "critical"
                })
    return issues


# =============================================================================
# CAMADA 3: Dicionário Anti-Typo (Fuzzy Match)
# =============================================================================

def check_terminology(text: str) -> list[dict]:
    """Verifica se o texto contém variações incorretas de termos."""
    issues = []
    text_lower = text.lower()

    for correct, variants in FOOTBALL_TERMS.items():
        for wrong in variants:
            if wrong.lower() in text_lower:
                issues.append({
                    "type": "terminology_error",
                    "wrong": wrong,
                    "correct": correct,
                    "detail": f"Termo incorreto '{wrong}' encontrado. Correto: '{correct}'.",
                    "severity": "medium"
                })
    return issues


def check_generic_placeholders(script_data: dict) -> list[dict]:
    """Detecta placeholders genéricos que a IA inventou."""
    issues = []
    generic_patterns = [
        r'Jogador\s*[A-Z]',       # "Jogador A", "Jogador B"
        r'Jogador\s+\d',           # "Jogador 1", "Jogador 2"
        r'Nome\s+\d',             # "Nome 1", "Nome 2"
        r'Jogador\s+desconhecido', # "Jogador desconhecido"
    ]

    # Checar gols
    for gol in script_data.get("gols", []):
        for pattern in generic_patterns:
            if re.search(pattern, gol, re.IGNORECASE):
                issues.append({
                    "type": "generic_placeholder",
                    "detail": f"Gol genérico detectado: '{gol}'. A IA inventou um nome.",
                    "field": "gols",
                    "severity": "high"
                })
                break

    # Checar artilheiros
    for art in script_data.get("artilheiros", script_data.get("artilheiras", [])):
        for pattern in generic_patterns:
            if re.search(pattern, art, re.IGNORECASE):
                issues.append({
                    "type": "generic_placeholder",
                    "detail": f"Artilheiro genérico detectado: '{art}'. A IA inventou um nome.",
                    "field": "artilheiros",
                    "severity": "high"
                })
                break

    return issues


# =============================================================================
# CAMADA 2: Cross-Reference via LLM (Groq - Rápido e Grátis)
# =============================================================================

async def llm_cross_check(source_text: str, script_text: str) -> dict:
    """
    Usa LLM (Groq) para comparar fonte vs roteiro e listar discrepâncias.
    Retorna {"valid": bool, "issues": [...]}
    """
    try:
        from app.routes.ai import call_groq, extract_json

        system = (
            "Você é um Fact-Checker especialista em esportes. "
            "Compare o TEXTO FONTE (verdade) com o ROTEIRO GERADO e liste APENAS erros factuais. "
            "NÃO critique estilo, tom ou estrutura — apenas FATOS ERRADOS."
        )

        prompt = (
            f"TEXTO FONTE (VERDADE):\n{source_text[:2000]}\n\n"
            f"ROTEIRO GERADO:\n{script_text[:1500]}\n\n"
            "Responda APENAS com JSON:\n"
            "{\n"
            '  "valid": true/false,\n'
            '  "issues": [\n'
            '    {"fact": "o que o roteiro diz", "correct": "o que a fonte diz", "severity": "critical|high|medium"}\n'
            "  ]\n"
            "}\n"
            "Se não houver erros factuais, retorne {\"valid\": true, \"issues\": []}."
        )

        resp = await call_groq(prompt, system)
        if resp:
            data = extract_json(resp)
            if data:
                return data

        logger.warning("[FACT-CHECK] LLM cross-check falhou, pulando camada 2")
        return {"valid": True, "issues": []}

    except Exception as e:
        logger.error(f"[FACT-CHECK] Erro no LLM cross-check: {e}")
        return {"valid": True, "issues": []}


# =============================================================================
# AUTO-CORREÇÃO
# =============================================================================

def apply_corrections(script_data: dict, issues: list[dict]) -> dict:
    """Aplica correções automáticas ao roteiro baseado nos issues encontrados."""
    corrected = script_data.copy()

    for issue in issues:
        # Corrigir placares errados
        if issue.get("type") == "wrong_score" and issue.get("correction"):
            old_score = issue.get("detail", "").split("'")[1] if "'" in issue.get("detail", "") else None
            new_score = issue["correction"]
            if old_score and new_score:
                # Corrigir no campo placar
                if corrected.get("placar") == old_score:
                    corrected["placar"] = new_score
                    logger.info(f"[FACT-CHECK] Placar corrigido: {old_score} → {new_score}")

                # Corrigir nos blocos de texto
                for block in corrected.get("blocks", []):
                    text = block.get("text", "")
                    # Substituir variações do placar no texto
                    old_verbal = old_score.replace("x", " a ")
                    new_verbal = new_score.replace("x", " a ")
                    if old_verbal in text:
                        block["text"] = text.replace(old_verbal, new_verbal)
                        logger.info(f"[FACT-CHECK] Texto corrigido: '{old_verbal}' → '{new_verbal}'")

        # Corrigir termos incorretos
        if issue.get("type") == "terminology_error":
            wrong = issue["wrong"]
            correct = issue["correct"]
            for block in corrected.get("blocks", []):
                text = block.get("text", "")
                if wrong in text:
                    block["text"] = text.replace(wrong, correct)
                    logger.info(f"[FACT-CHECK] Termo corrigido: '{wrong}' → '{correct}'")
            # Corrigir no título também
            if wrong in corrected.get("title", ""):
                corrected["title"] = corrected["title"].replace(wrong, correct)

        # Limpar placeholders genéricos
        if issue.get("type") == "generic_placeholder":
            field = issue.get("field")
            if field == "gols":
                corrected["gols"] = []
                logger.info("[FACT-CHECK] Gols genéricos removidos (campo zerado)")
            elif field == "artilheiros":
                corrected["artilheiros"] = []
                logger.info("[FACT-CHECK] Artilheiros genéricos removidos (campo zerado)")

    return corrected


# =============================================================================
# FUNÇÃO PRINCIPAL: validate_script
# =============================================================================

async def validate_script(source_text: str, script_data: dict, use_llm: bool = True) -> dict:
    """
    Executa as 3 camadas de validação do Fact Guard.

    Args:
        source_text: Texto original da notícia (fonte de verdade)
        script_data: Dicionário do roteiro gerado pela IA
        use_llm: Se True, usa LLM para cross-check (Camada 2)

    Returns:
        {
            "valid": bool,
            "issues": [...],
            "corrected_data": dict (roteiro com correções aplicadas),
            "layers": {"regex": [...], "llm": [...], "dictionary": [...]}
        }
    """
    all_issues = []

    # --- Camada 1: Regex Claims ---
    source_scores = extract_scores(source_text)
    script_full_text = " ".join([b.get("text", "") for b in script_data.get("blocks", [])])
    script_scores = extract_scores(script_full_text)

    score_issues = compare_scores(source_scores, script_scores)
    placeholder_issues = check_generic_placeholders(script_data)
    regex_issues = score_issues + placeholder_issues

    # --- Camada 3: Dicionário (roda antes do LLM porque é instantâneo) ---
    dict_issues = check_terminology(script_full_text)
    # Verificar também o título
    dict_issues += check_terminology(script_data.get("title", ""))

    all_issues.extend(regex_issues)
    all_issues.extend(dict_issues)

    # --- Camada 2: LLM Cross-Check (só se ativado) ---
    llm_issues = []
    if use_llm and source_text:
        llm_result = await llm_cross_check(source_text, script_full_text)
        if not llm_result.get("valid", True):
            for issue in llm_result.get("issues", []):
                llm_issues.append({
                    "type": "llm_factual_error",
                    "detail": f"Roteiro diz: '{issue.get('fact', '?')}'. Correto: '{issue.get('correct', '?')}'.",
                    "severity": issue.get("severity", "high")
                })
            all_issues.extend(llm_issues)

    # --- Auto-Correção ---
    corrected_data = apply_corrections(script_data, all_issues) if all_issues else script_data

    is_valid = len(all_issues) == 0

    if all_issues:
        logger.warning(
            "[FACT-CHECK] %d issue(s) encontrada(s): %s",
            len(all_issues),
            [i.get("type") for i in all_issues]
        )
    else:
        logger.info("[FACT-CHECK] ✅ Roteiro validado — nenhum erro factual detectado.")

    return {
        "valid": is_valid,
        "total_issues": len(all_issues),
        "issues": all_issues,
        "corrected_data": corrected_data,
        "layers": {
            "regex": regex_issues,
            "llm": llm_issues,
            "dictionary": dict_issues
        }
    }
