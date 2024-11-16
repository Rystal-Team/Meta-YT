from typing import Dict, List


def convert_to_srt(transcript: List[Dict[str, float]]) -> str:
    """
    Convert a transcript to SubRip (SRT) format.

    :param transcript: The transcript to convert.
    :type transcript: list
    :return: The transcript in SubRip (SRT) format.
    :rtype: str
    """
    srt_output = ""

    for index, item in enumerate(transcript):
        start_time = format_time(item["start"])
        end_time = format_time(item["end"])
        text = item["text"]

        srt_output += f"{index + 1}\n"
        srt_output += f"{start_time} --> {end_time}\n"
        srt_output += f"{text}\n\n"

    return srt_output


def format_time(seconds: float) -> str:
    """
    Format the time in 'HH:MM:SS,MS' format for SRT.

    :param seconds: The time in seconds.
    :type seconds: float
    :return: The formatted time.
    :rtype: str
    """

    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds_remaining = seconds % 60
    milliseconds = round((seconds_remaining - int(seconds_remaining)) * 1000)

    return f"{hours:02}:{minutes:02}:{int(seconds_remaining):02},{milliseconds:03}"
