
import sys
import os
# Ensure valid import path for sibling package
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import argparse
from tiktok_uploader.upload import upload_video, upload_videos
from tiktok_uploader.auth import verify_cookies

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="Command to perform", choices=["upload", "show"])
    parser.add_argument("-u", "--user", help="TikTok username", required=True)
    parser.add_argument("-v", "--video", help="Video file path")
    parser.add_argument("-t", "--title", help="Video title")
    parser.add_argument("-vi", "--visibility", help="Video visibility", choices=["0", "1", "2"], default="0")
    parser.add_argument("-ct", "--comment_on_tiktok", help="Allow comments", choices=["0", "1"], default="1")
    parser.add_argument("-d", "--duet", help="Allow duets", choices=["0", "1"], default="0")
    parser.add_argument("-st", "--stitch", help="Allow stitch", choices=["0", "1"], default="0")
    parser.add_argument("-sd", "--schedule_time", help="Schedule time (epoch seconds)", default="0")
    parser.add_argument("-a", "--auth", help="Auth mode", choices=["cookie"], default="cookie")
    args = parser.parse_args()

    if args.command == "upload":
        if not args.video or not args.title:
            print("Error: Video and title are required for upload.")
            return

        upload_video(
            filename=args.video,
            description=args.title,
            username=args.user,
            cookies=f"CookiesDir/tiktok_session-{args.user}.cookie",
            schedule_time=int(args.schedule_time)
        )
    elif args.command == "show":
        # Placeholder for show command if needed
        pass

if __name__ == "__main__":
    main()
