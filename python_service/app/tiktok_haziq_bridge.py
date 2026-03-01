import os
import sys
import argparse
import asyncio
from tiktokautouploader import upload_tiktok

def main():
    parser = argparse.ArgumentParser(description="Ponte TikTokAutoUploader (Haziq-exe)")
    parser.add_argument("--video", help="Caminho do vídeo")
    parser.add_argument("--title", help="Título do vídeo")
    parser.add_argument("--account", default="futebas_oficial", help="Nome da conta (para persistência de cookies)")
    parser.add_argument("--hashtags", nargs="*", default=[], help="Lista de hashtags")
    parser.add_argument("--sound", help="Nome do áudio nativo do TikTok (opcional, mas recomendado)")
    parser.add_argument("--setup", action="store_true", help="Abre o navegador para login manual")
    parser.add_argument("--headless", action="store_true", default=False, help="Executar em modo headless (padrão False para permitir setup)")
    
    args = parser.parse_args()

    try:
        if args.setup:
            print(f"[haziq-bridge] 🔑 MODO SETUP: Iniciando navegador HEADFUL para login manual...")
            # Chamamos com um vídeo dummy ou apenas forçamos a abertura
            # A lib exige um vídeo para a maioria das funções, vamos ignorar erros se for setup
            try:
                upload_tiktok(
                    video=None, 
                    description="Setup Account",
                    accountname=args.account,
                    headless=False, # Forçamos True se via API mas pro usuário ver
                    stealth=True
                )
            except Exception as e:
                if "video" in str(e).lower() or "Success" in str(e):
                    print(f"[haziq-bridge] ✅ Setup finalizado. Verifique se os cookies foram salvos em /data_midia.")
                else:
                    raise e
            return

        if not args.video or not args.title:
            parser.error("Os argumentos --video e --title são obrigatórios se não estiver em modo --setup.")

        print(f"[haziq-bridge] Iniciando upload via TikTokAutoUploader...")
        upload_tiktok(
            video=args.video,
            description=args.title,
            accountname=args.account,
            hashtags=args.hashtags,
            sound_name=args.sound if args.sound else None,
            sound_aud_vol='main' if args.sound else 'mix',
            headless=True, # Automação real é headless
            stealth=True
        )
        
        print("[haziq-bridge] ✅ Processo finalizado!")
        sys.exit(0)
    except Exception as e:
        print(f"[haziq-bridge] ❌ Finalizado com nota: {str(e)}")
        sys.exit(0) if "Success" in str(e) or "Completed" in str(e) else sys.exit(1)

if __name__ == "__main__":
    main()
