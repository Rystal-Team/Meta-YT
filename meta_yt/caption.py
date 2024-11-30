"""This module contains the developer interface for captions fetching."""

from html import unescape

import requests
import xmltodict

from .langauge import get_language
from .srt import convert_to_srt


class Caption:
    """
    A class to represent video captions and process them.

    :param baseUrl: The base URL of the video.
    :type baseUrl: str
    :param language_code: The ISO 639-1 language code of the captions.
    :type language_code: str
    :param auto_generated: A boolean indicating if the captions are auto-generated.
    :type auto_generated: bool
    """

    def __init__(self, baseUrl: str, language_code: str, auto_generated: bool):
        """
        Initialize a Caption object.

        :param baseUrl: The base URL of the video.
        :type baseUrl: str
        :param language_code: The ISO 639-1 language code of the captions.
        :type language_code: str
        :param auto_generated: A boolean indicating if the captions are auto-generated.
        :type auto_generated: bool
        """
        self.url = f"https://youtube.com{baseUrl}"
        self.language_code = language_code
        self.language = get_language(language_code)
        self.auto_generated = auto_generated
        self.__transcript = []

        response = requests.get(self.url, timeout=5)
        self.xml_script = xmltodict.parse(response.content)

        for block in self.xml_script["transcript"]["text"]:
            line = {
                "text": unescape(block.get("#text", "")),
                "start": float(block["@start"]),
                "end": round(float(block["@start"]) + float(block["@dur"]), 3),
                "duration": float(block["@dur"]),
            }
            self.__transcript.append(line)

    def to_srt(self) -> str:
        """
        Convert transcript to SubRip (SRT) format.

        :return: The transcript in SubRip (SRT) format.
        :rtype: str
        """

        return convert_to_srt(self.__transcript)

    @property
    def transcript(self) -> list:
        """
        Get the transcript of the video.

        :return: A list containing dictionaries representing each line of the transcript.
        :rtype: list
        """
        return self.__transcript
