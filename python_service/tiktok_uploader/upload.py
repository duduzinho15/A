import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Mock TikTok Uploader")
    parser.add_argument("-v", "--video", help="Video path", required=False)
    parser.add_argument("-t", "--title", help="Title/Description", required=False)
    parser.add_argument("-c", "--cookies", help="Cookies path", required=False)
    
    args = parser.parse_args()
    
    print(f"[Mock] Simulating upload for video: {args.video}")
    print(f"[Mock] Title: {args.title}")
    print("[Mock] Upload Success! (This is a placeholder script)")
    
    # Simula status de sucesso para o publish.py ler
    sys.exit(0)

if __name__ == "__main__":
    main()
