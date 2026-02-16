
import time
import datetime
import random
import requests
from urllib.parse import urlencode

from tiktok_uploader.auth import Auth
from tiktok_uploader.config import Config
from tiktok_uploader.utils import bold, green, red, check_valid_path, get_image_size

class TikTok:
    def __init__(self, cookies=None, proxy=None):
        self.auth = Auth(cookies, proxy)

    def upload_video(self, video_path, description, cookies=None, proxy=None):
        self.auth = Auth(cookies, proxy)
        return self.upload_video(video_path, description)

    def get_video_id(self, video_path):
        return get_image_size(video_path)

    def check_valid_path(self, video_path):
        return check_valid_path(video_path)
