"""This module contains the developer interface for captions fetching."""

# Import necessary modules
import requests  # Module for making HTTP requests
import xmltodict  # Module for parsing XML data
from .langauge import get_language  # Importing custom function for getting language names from language codes
from html import unescape

class Caption:
    def __init__(self, baseUrl: str, language_code: str):
        """
        Initialize a Caption object.

        Args:
            baseUrl (str): The base URL of the video.
            language_code (str): The ISO 639-1 language code of the captions.
        """
        # Construct the full URL for fetching captions
        self.url = "https://youtube.com{baseUrl}".format(baseUrl=baseUrl)
        # Store the language code
        self.language_code = language_code
        # Get the language name from the language code
        self.language = get_language(language_code)
        # Initialize an empty list to store transcript lines
        self.__transcript = []

        # Make a GET request to the caption URL
        response = requests.get(self.url)
        # Parse the XML response
        self.xml_script = xmltodict.parse(response.content)

        # Iterate through each text block in the transcript
        for block in self.xml_script["transcript"]["text"]:
            # Extract relevant information for each line
            line = {
                "text": unescape(block["#text"]),
                "start": float(block["@start"]),
                "end": round(float(block["@start"]) + float(block["@dur"]), 3),
                "duration": float(block["@dur"]),
            }

            # Append the line to the transcript list
            self.__transcript.append(line)

    def to_srt(self) -> str:
        """
        Convert transcript to SubRip (SRT) format.

        Returns:
            str: The transcript in SubRip (SRT) format.
        """
        self.__transcript
        return

    @property
    def transcript(self) -> list:
        """
        Get the transcript of the video.

        Returns:
            list: A list containing dictionaries representing each line of the transcript.
        """
        return self.__transcript
