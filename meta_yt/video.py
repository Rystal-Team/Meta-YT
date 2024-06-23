"""This module contains the developer interface for video fetching."""

import requests
from .caption import Caption


class Video:
    def __init__(self, videoId: str, retries=5):
        """
        The function initializes a class instance with video details fetched from the YouTube API.

        Arguments:

        * `videoId`: The ID of the YouTube video used to fetch its details.
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
                self.video_id = video_id # ID of the video.
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
        The function `get_captions` retrieves caption tracks from metadata, filtering out auto-generated
        captions based on the `include_generated` parameter.

        Arguments:

        * `include_generated`: The `include_generated` parameter is a boolean flag that determines
        whether auto-generated captions should be included in the result or not. If `include_generated`
        is set to `True`, then all captions, including auto-generated ones, will be returned. If set to
        `False`, auto-generated captions will be

        Returns:

        A dictionary of Caption objects, where the keys are the language codes of the captions.
        """
        caption_tracks = self.metadata["captions"]["playerCaptionsTracklistRenderer"][
            "captionTracks"
        ]

        captions = {}
        # This block of code is iterating over each caption track in the `caption_tracks` list
        # obtained from the video metadata. It checks if the caption track is auto-generated based on
        # the presence of the term "auto-generated" in the caption track's name.
        for track in caption_tracks:
            if (
                "auto-generated" in track["name"]["runs"][0]["text"]
                and not include_generated
            ):
                continue
            caption = Caption(
                track["baseUrl"],
                track["languageCode"],
            )
            captions[caption.language] = caption

        return captions
