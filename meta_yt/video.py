"""This module contains the developer interface for video fetching."""

import requests
from .caption import Caption


class Video:
    """
    A class to represent a YouTube video and fetch its details using the YouTube API.

    :param videoId: The ID of the YouTube video used to fetch its details.
    :type videoId: str
    :param retries: The number of retry attempts for fetching video details. Defaults to 5.
    :type retries: int
    """

    def __init__(self, videoId: str, retries=5):
        """
        Initialize a Video object with details fetched from the YouTube API.

        :param videoId: The ID of the YouTube video used to fetch its details.
        :type videoId: str
        :param retries: The number of retry attempts for fetching video details. Defaults to 5.
        :type retries: int
        """
        url = "https://www.youtube.com/youtubei/v1/player"
        params = {
            "videoId": videoId,
            "key": "AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8",
            "contentCheckOk": "True",
            "racyCheckOk": "True",
        }
        json_data = {
            "context": {
                "client": {
                    "clientName": "MWEB",
                    "clientVersion": "2.20211109.01.00",
                }
            },
            "api_key": "AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8",
        }

        for attempt in range(retries):
            try:
                response = requests.post(url, params=params, json=json_data)
                response.raise_for_status()
                data = response.json()["videoDetails"]

                # Extracting specific video details from the response data.
                video_id = data["videoId"]
                channel_id = data["channelId"]
                thumbnails = data["thumbnail"]["thumbnails"]

                # Assigning extracted video details to instance variables.
                self.url = f"https://youtu.be/{video_id}"  # URL of the YouTube video.
                self.title = data["title"]  # Title of the video.
                self.video_id = video_id  # ID of the video.
                self.channel = data["author"]  # Channel name of the video.
                self.duration = int(data["lengthSeconds"])  # Duration of the video.
                self.views = int(data["viewCount"])  # Number of views on the video.
                self.thumbnail = thumbnails[-1]["url"]  # URL of the video thumbnail.
                self.thumbnails = thumbnails  # List of thumbnails of the video.
                self.channel_url = f"https://www.youtube.com/channel/{channel_id}"  # URL of the video channel.
                self.metadata = (
                    response.json()
                )  # Additional metadata fetched from the YouTube API.

                return  # Exit
            except (requests.RequestException, KeyError) as e:
                if attempt < retries - 1:
                    pass
                else:
                    raise e

    def get_captions(self, include_generated: bool = False):
        """
        Retrieve caption tracks from metadata, filtering out auto-generated captions based on the `include_generated` parameter.

        :param include_generated: A boolean flag that determines whether auto-generated captions should be included in the result or not. If set to `True`, all captions, including auto-generated ones, will be returned. If set to `False`, auto-generated captions will be excluded. Defaults to False.
        :type include_generated: bool
        :return: A dictionary of Caption objects, where the keys are the language codes of the captions.
        :rtype: dict
        """
        return {Caption(track["baseUrl"], track["languageCode"]).language: Caption(track["baseUrl"], track["languageCode"]) for track in self.metadata.get("captions", {}).get("playerCaptionsTracklistRenderer", {}).get("captionTracks", []) if "auto-generated" not in track.get("name", {}).get("runs", [{}])[0].get("text", "") or include_generated}
