
import sys
import os
import argparse
import traceback

# Ensure the library is in path
sys.path.append('/app/tiktok_uploader')

try:
    from tiktok_uploader.tiktok import upload_video
except ImportError:
    print("Error: Could not import upload_video function. Checking path...")
    print(sys.path)
    traceback.print_exc()
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Custom TikTok Uploader")
    parser.add_argument("--video", required=True, help="Path to video file")
    parser.add_argument("--title", required=True, help="Video title/description")
    parser.add_argument("--cookies", help="Path to cookies file (unused by lib, uses session_user)")
    parser.add_argument("--user", help="Session user name (default: auto)", default="auto")
    parser.add_argument("--proxy", help="Proxy URL", default=None)
    
    args = parser.parse_args()
    
    # upload_video signature:
    # def upload_video(session_user, video, title, schedule_time=0, allow_comment=1, allow_duet=0, allow_stitch=0, visibility_type=0, ...)
    
    try:
        print(f"Uploading {args.video} for user {args.user}...")
        
        # Privacy mapping: 0=public, 1=private/friends? 
        # Lib says: visibility_type=0. 
        # CLI usage: -vi 0 (Public), 1 (Private), 2 (Friends)
        
        # We need to ensure cookies exist where library expects them.
        # Lib uses: load_cookies_from_file(f"tiktok_session-{session_user}")
        # It looks in current working directory? Or relative to cookies.py?
        # publish.py saves to TIKTOK_COOKIES_DIR = /app/tiktok_uploader/CookiesDir
        # I might need to symlink or move cookies if the lib assumes CWD.
        # But let's try assuming lib is smart or configures paths.
        
        result = upload_video(
            session_user=args.user,
            video=args.video,
            title=args.title,
            visibility_type=0, # Public by default for now
            proxy=args.proxy
        )
        
        if result == False:
             print("Upload returned False.")
             sys.exit(1)
             
        print("Upload finished.")
        print(f"Result: {result}")
        
    except Exception as e:
        print("Exception during upload:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
