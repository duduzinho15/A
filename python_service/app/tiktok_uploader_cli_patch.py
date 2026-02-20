"""
tiktok_uploader_cli_patch.py — CLI Wrapper para TikTok Uploader
================================================================
CORREÇÃO v2.0: Removido import inexistente `tiktok_uploader.auth.verify_cookies`
que causava ModuleNotFoundError. A biblioteca TikTokAutoUploader não expõe
mais esse módulo diretamente após atualizações. Usamos apenas `upload_video`
do módulo `upload` que é a API estável da biblioteca.
"""

import sys
import os
import argparse
import traceback

# Adiciona o diretório pai ao path para resolver imports relativos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import correto — único ponto de entrada estável da biblioteca
try:
    from tiktok_uploader.upload import upload_video, upload_videos
except ImportError:
    # Fallback: tenta o módulo customizado que usa a fork local da lib
    try:
        sys.path.append("/app/tiktok_uploader")
        from tiktok_uploader.tiktok import upload_video
        print("[TikTok CLI] Usando fork local da lib (tiktok_uploader.tiktok).")
    except ImportError as e:
        print(f"[TikTok CLI] ERRO CRÍTICO: Não foi possível importar TikTok Uploader: {e}")
        print("[TikTok CLI] Verifique se a biblioteca está instalada em requirements.txt")
        traceback.print_exc()
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="CLI para upload de vídeos no TikTok via cookie de sessão."
    )
    parser.add_argument("command", choices=["upload", "show"],
                        help="Comando: 'upload' para enviar vídeo, 'show' para verificar autenticação.")
    parser.add_argument("-u", "--user", required=True,
                        help="Username do TikTok (deve ter cookie salvo em CookiesDir/).")
    parser.add_argument("-v", "--video", help="Caminho do arquivo de vídeo .mp4")
    parser.add_argument("-t", "--title", help="Título/descrição do vídeo")
    parser.add_argument("-vi", "--visibility", choices=["0", "1", "2"], default="0",
                        help="Visibilidade: 0=Público, 1=Amigos, 2=Privado")
    parser.add_argument("-ct", "--comment_on_tiktok", choices=["0", "1"], default="1",
                        help="Permitir comentários: 1=Sim, 0=Não")
    parser.add_argument("-d", "--duet", choices=["0", "1"], default="0",
                        help="Permitir duet: 1=Sim, 0=Não")
    parser.add_argument("-st", "--stitch", choices=["0", "1"], default="0",
                        help="Permitir stitch: 1=Sim, 0=Não")
    parser.add_argument("-sd", "--schedule_time", default="0",
                        help="Agendamento em epoch seconds (0 = publicar agora)")
    parser.add_argument("-a", "--auth", choices=["cookie"], default="cookie",
                        help="Modo de autenticação (somente 'cookie' suportado)")
    args = parser.parse_args()

    if args.command == "upload":
        if not args.video or not args.title:
            print("[TikTok CLI] Erro: --video e --title são obrigatórios para upload.")
            sys.exit(1)

        cookies_path = f"CookiesDir/tiktok_session-{args.user}.cookie"
        print(f"[TikTok CLI] Enviando '{args.video}' para @{args.user}...")
        print(f"[TikTok CLI] Cookies: {cookies_path}")

        try:
            upload_video(
                filename=args.video,
                description=args.title,
                username=args.user,
                cookies=cookies_path,
                schedule_time=int(args.schedule_time),
            )
            print("[TikTok CLI] Upload concluído com sucesso!")
        except Exception as e:
            print(f"[TikTok CLI] Erro durante o upload: {e}")
            traceback.print_exc()
            sys.exit(1)

    elif args.command == "show":
        # Verifica se o cookie existe — sem chamar verify_cookies que não existe mais
        cookies_path = f"CookiesDir/tiktok_session-{args.user}.cookie"
        if os.path.exists(cookies_path):
            print(f"[TikTok CLI] Cookie encontrado: {cookies_path} ✓")
        else:
            print(f"[TikTok CLI] AVISO: Cookie não encontrado em: {cookies_path}")
            print("[TikTok CLI] Execute a autenticação manual para gerar o cookie.")
            sys.exit(1)


if __name__ == "__main__":
    main()
