import re
from enum import Enum

from requests.exceptions import MissingSchema
from requests.models import PreparedRequest
from userbot.utils import runcmd


class Stream(Enum):
    audio = 1
    video = 2


yt_regex_str = "^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"

yt_regex = re.compile(yt_regex_str)


def check_url(url):
    prepared_request = PreparedRequest()
    try:
        prepared_request.prepare_url(url, None)
        return prepared_request.url
    except MissingSchema:
        return False


async def get_yt_stream_link(url, audio_only=False):
    if audio_only:
        return (await runcmd(f"yt-dlp --no-warnings -f bestaudio -g {url}"))[0]
    (await runcmd(f"yt-dlp --no-warnings -f best -g {url}"))[0]
