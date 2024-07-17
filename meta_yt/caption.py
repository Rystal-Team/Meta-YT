"""This module contains the developer interface for captions fetching."""

import requests  
import xmltodict 
from .langauge import get_language 
from html import unescape

class Caption:
    """
    A class to represent video captions and process them.

    :param baseUrl: The base URL of the video.
    :type baseUrl: str
    :param language_code: The ISO 639-1 language code of the captions.
    :type language_code: str
    """

    def __init__(self, baseUrl: str, language_code: str):
        """
        Initialize a Caption object.

        :param baseUrl: The base URL of the video.
        :type baseUrl: str
        :param language_code: The ISO 639-1 language code of the captions.
        :type language_code: str
        """
        self.url = "https://youtube.com{baseUrl}".format(baseUrl=baseUrl)
        self.language_code = language_code
        self.language = get_language(language_code)
        self.__transcript = []

        response = requests.get(self.url)
        self.xml_script = xmltodict.parse(response.content)

        for block in self.xml_script["transcript"]["text"]:
            line = {
                "text": unescape(block["#text"]),
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
        self.__transcript
        return

    @property
    def transcript(self) -> list:
        """
        Get the transcript of the video.

        :return: A list containing dictionaries representing each line of the transcript.
        :rtype: list
        """
        return self.__transcript