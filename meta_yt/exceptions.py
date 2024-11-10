class MetaYTError(Exception):
    """
    Base exception for inheritance.
    """

    pass


class VideoUnavailable(MetaYTError):
    """
    Exception raised when a video is unavailable.

    :param videoId: The ID of the unavailable video.
    :type videoId: str
    """

    def __init__(self, videoId: str):
        """
        Initializes a `VideoUnavailable` exception instance.

        :param videoId: The ID of the unavailable video.
        :type videoId: str
        """
        self.videoId = videoId
        super().__init__(self.error_message)

    @property
    def error_message(self) -> str:
        """
        Returns the error message for the VideoUnavailable exception.

        :return: The error message explaining why the video is unavailable.
        :rtype: str
        """
        return (
            f"Video ID: `{self.videoId}` is unavailable, it might be caused by various reasons such as:\n"
            "- Invalid Video ID\n"
            "- Video is private\n"
            "- Video is region locked"
        )
