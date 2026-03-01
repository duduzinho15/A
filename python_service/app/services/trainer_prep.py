def format_to_jsonl(row: dict) -> dict:
    """
    Converte uma linha do banco para o formato de instrução (Alpaca/ShareGPT style).
    """
    metrics = row.get('metrics', {})
    ctr = metrics.get('ctr', 0)
    
    return {
        "instruction": "Escreva um roteiro de video curto e viral para redes sociais baseado no conteudo fornecido.",
        "input": str(row.get('raw_content', '')),
        "output": f"TITULO: {row.get('title', '')}\n\nROTEIRO:\n{row.get('script', '')}",
        "metadata": {
            "ctr": ctr,
            "source": "content_factory_success_loop"
        }
    }
