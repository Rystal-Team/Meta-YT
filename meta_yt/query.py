import requests, json  # Modules for making HTTP requests and parsing JSON data
import urllib.parse  # Module for URL encoding


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
        self.query = query
        self.max_results = max_results
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
            try:
                for video in contents["itemSectionRenderer"]["contents"]:
                    if "videoRenderer" in video.keys():
                        try:
                            result = {}
                            result["title"] = video["videoRenderer"]["title"]["runs"][
                                0
                            ]["text"]
                            result["videoId"] = video["videoRenderer"]["videoId"]
                            self.__results.append(result)
                        except Exception:
                            continue
            except Exception:
                continue

    def __search__(self):
        """Perform a YouTube search and parse the results."""
        encoded_query = urllib.parse.quote_plus(self.query)  # Encode the search query
        query_url = f"https://youtube.com/results?search_query={encoded_query}"  # Construct the search URL
        response = requests.get(query_url)  # Send a GET request to the search URL

        while "ytInitialData" not in response.text:
            response = requests.get(query_url)

        self.__parse__(response.text)  # Parse the search response

    @property
    def results(self) -> list | None:
        """
        Get the search results.

        :return: A list containing the search results or None if no results are found.
        :rtype: list | None
        """
        return self.__results[
            : self.max_results
        ]  # Return the results, limited by the max_results count
