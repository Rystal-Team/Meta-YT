class MetaYTError(Exception):
    """Base exception for inheritance."""


class VideoUnavailable(MetaYTError):
    """Exception `VideoUnavailable`"""

    def __init__(self, videoId: str):
        """
        Initializes a `VideoUnavailable` exception instance.

        Args:
            videoId (str): The ID of the unavailable video.
        """
        self.videoId = videoId
        super().__init__(self.error_message)

    @property
    def error_message(self):
        """
        Returns the error message for the VideoUnavailable exception.

        Returns:
            str: The error message explaining why the video is unavailable.
        """
        return (
            f"Video ID: `{self.videoId}` is unavailable, it might be caused by various reasons such as:\n"
            "- Invalid Video ID\n"
            "- Video is private\n"
            "- Video is region locked"
        )
