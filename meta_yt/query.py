import requests, json  # Modules for making HTTP requests and parsing JSON data
import urllib.parse  # Module for URL encoding


class Query:
    def __init__(self, query: str, max_results: int = None):
        """
        Initialize a Query object.

        Args:
            query (str): The search query.
            max_results (int, optional): The maximum number of results to retrieve. Defaults to None.
        """
        self.query = query  # Store the search query
        self.max_results = max_results  # Store the maximum number of results
        self.__results = []  # Initialize an empty list to store search results
        self.__search__()  # Perform the search

    def __parse__(self, response: str):
        """
        Parse the YouTube search response and extract video information.

        Args:
            response (str): The raw HTML response from the YouTube search.

        Returns:
            None
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
        """
        Perform a YouTube search and parse the results.

        Returns:
            None
        """
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

        Returns:
            list | None: A list containing the search results or None if no results are found.
        """
        return self.__results[
            : self.max_results
        ]  # Return the results, limited by the max_results count
