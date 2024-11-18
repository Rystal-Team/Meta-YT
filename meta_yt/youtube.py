"""This module provides the highest level interface in this module, allowing interactions with `Video`, `Caption` and `Playlist`"""

from typing import Optional

# Import necessary modules
from urllib import parse  # Module for URL parsing

from .query import Query  # Importing the Query class for performing YouTube searches
from .video import Video  # Importing the Video class for handling YouTube videos


def check_isPlaylist(url: str) -> bool:
    """
    Check if a given URL corresponds to a YouTube playlist.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL corresponds to a playlist, False otherwise.
    """
    return ("playlist?" in url) or ("list=" in url)


def get_video_id(url: str) -> Optional[str]:
    """
    Extract the video ID from a YouTube video URL.

    Args:
        url (str): The YouTube video URL.

    Returns:
        Optional[str]: The video ID if found, None otherwise.
    """
    query = parse.urlparse(url)
    if query.hostname == "youtu.be":
        return query.path[1:]
    if query.hostname in {"www.youtube.com", "youtube.com"}:
        if query.path == "/watch":
            p = parse.parse_qs(query.query)
            return p["v"][0]
        if query.path[:7] == "/embed/":
            return query.path.split("/")[2]
        if query.path[:3] == "/v/":
            return query.path.split("/")[2]
    return None


class YouTube:
    def __init__(self, query: str):
        """
        Initialize a YouTube object.

        Args:
            query (str): The search query or video URL.
        """
        self.video = None
        result = get_video_id(query)

        if result is None:
            results = Query(query, max_results=1).results
            self.videoId = results[0]["videoId"]
        else:
            self.videoId = result

        self.video = Video(self.videoId)
