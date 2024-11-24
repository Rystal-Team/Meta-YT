import json
import urllib.parse  # Module for URL encoding

import requests


class Query:
    """
    A class to perform YouTube search queries and extract video information.

    :param query: The search query.
    :type query: str
    :param max_results: The maximum number of results to retrieve. Defaults to None.
    :type max_results: int, optional
    """

    def __init__(self, query: str, max_results: int = None):
        """
        Initialize a Query object.

        :param query: The search query.
        :type query: str
        :param max_results: The maximum number of results to retrieve. Defaults to None.
        :type max_results: int, optional
        """
        self.max_results = max_results
        self.__query = query
        self.__results = []
        self.__search__()

    def __parse__(self, response: str):
        """
        Parse the YouTube search response and extract video information.

        :param response: The raw HTML response from the YouTube search.
        :type response: str
        """
        start_index = response.index("ytInitialData") + len("ytInitialData") + 3
        end_index = response.index("};", start_index) + 1

        data = json.loads(response[start_index:end_index])

        for contents in data["contents"]["twoColumnSearchResultsRenderer"][
            "primaryContents"
        ]["sectionListRenderer"]["contents"]:
            for video in contents.get("itemSectionRenderer", {}).get("contents", []):
                if "videoRenderer" in video.keys():
                    try:
                        result = {
                            "title": video["videoRenderer"]["title"]["runs"][0]["text"],
                            "videoId": video["videoRenderer"]["videoId"],
                        }
                        self.__results.append(result)
                    except KeyError:
                        continue

    def __search__(self):
        """Perform a YouTube search and parse the results."""
        encoded_query = urllib.parse.quote_plus(self.__query)
        query_url = f"https://youtube.com/results?search_query={encoded_query}"
        response = requests.get(query_url)

        retry_limit = 50
        retry_count = 0

        while "ytInitialData" not in response.text and retry_count < retry_limit:
            response = requests.get(query_url)
            retry_count += 1

        self.__parse__(response.text)

    @property
    def results(self) -> list | None:
        """
        Get the search results.

        :return: A list containing the search results or None if no results are found.
        :rtype: list | None
        """
        return self.__results[: self.max_results]
