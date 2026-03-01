import logging
import os
from typing import List, Tuple
from PIL import Image

logger = logging.getLogger("visual_gate")

class VisualGate:
    """
    Validador Semântico de Imagens (Nível 3).
    Usa o modelo CLIP para garantir que a imagem baixada tem relação 
    real com o tema do vídeo (ex: futebol, estádio, jogador).
    """
    
    _model = None
    _processor = None

    @classmethod
    def _get_model(cls):
        if cls._model is None:
            try:
                from transformers import CLIPProcessor, CLIPModel
                model_id = "openai/clip-vit-base-patch32"
                logger.info("[VisualGate] Carregando modelo CLIP (%s) no container...", model_id)
                cls._model = CLIPModel.from_pretrained(model_id)
                cls._processor = CLIPProcessor.from_pretrained(model_id)
                logger.info("[VisualGate] Modelo CLIP carregado com sucesso.")
            except Exception as e:
                logger.error("[VisualGate] Falha ao carregar CLIP: %s", e)
                return None, None
        return cls._model, cls._processor

    @classmethod
    def score_relevance(cls, image_path: str, labels: List[str]) -> List[Tuple[str, float]]:
        """
        Calcula o score de similaridade entre a imagem e uma lista de labels.
        Ex: labels = ["futebol", "praia", "estátua"]
        """
        model, processor = cls._get_model()
        if not model or not processor:
            return []

        try:
            image = Image.open(image_path).convert("RGB")
            inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)
            outputs = model(**inputs)
            
            # Probabilidades via Softmax (0 a 1)
            probs = outputs.logits_per_image.softmax(dim=1)
            results = []
            for i, label in enumerate(labels):
                score = float(probs[0][i]) * 100
                results.append((label, score))
            
            return sorted(results, key=lambda x: x[1], reverse=True)
        except Exception as e:
            logger.error("[VisualGate] Erro ao processar imagem %s: %s", image_path, e)
            return []

    @classmethod
    def is_relevant(cls, image_path: str, tema: str = "futebol", threshold: float = 65.0) -> bool:
        """
        Versão binária: A imagem é do tema proposto?
        Compara o tema proposto contra um 'ruído' genérico.
        """
        # Comparamos o tema real contra temas que queremos evitar (ruído e placeholders)
        labels = [
            tema, 
            "landscape architecture", 
            "beach and travel", 
            "statue or art",
            "blank white background",
            "generic abstract pattern",
            "blank gray square",
            "placeholder image dummy",
            "text only logo",
            "website screenshot"
        ]
        scores = cls.score_relevance(image_path, labels)
        
        if not scores:
            return True # Fallback: se a IA falhar, aceitamos (melhor que vídeo vazio)

        top_label, top_score = scores[0]
        logger.info("[VisualGate] Image %s -> Top: %s (%.1f%%)", os.path.basename(image_path), top_label, top_score)
        
        # Se o tema de futebol não for o vencedor absoluto, ou o vencedor não for o tema com confidence OK, rejeita
        if top_label == tema and top_score >= threshold:
            return True
        
        logger.warning("[VisualGate] Imagem '%s' descartada (Venceu: %s com %.1f%%)", os.path.basename(image_path), top_label, top_score)
        return False
