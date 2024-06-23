# Meta-YT
<br />
<div align="center">
  <a href="https://github.com/Rystal-Team/Rystal-V6/blob/main/assets/logo.png?raw=true">
    <img src="./assets/logo.png" alt="Logo" width="80" height="80">
  </a>
  <h3 align="center">Rystal V6</h3>
  <p align="center">
    Meta-YT is a lightweight Python library for fetching YouTube video metadata. It allows users to interact with YouTube videos, captions, and playlists, making it easier to retrieve information and captions from YouTube.
    <br />
    <br />  
    <a href="https://github.com/Rystal-Team/Rystal-V6/issues">Submit Issues</a> · <a href="https://github.com/Rystal-Team/Rystal-V6/releases">Releases</a>
  </p>
</div>

<div align="center">

  [![GitHub Forks](https://img.shields.io/github/forks/Rystal-Team/Rystal-V6.svg?style=for-the-badge)](https://github.com/Rystal-Team/Rystal-V6)
  [![GitHub Stars](https://img.shields.io/github/stars/Rystal-Team/Rystal-V6.svg?style=for-the-badge)](https://github.com/Rystal-Team/Rystal-V6)
  [![License](https://img.shields.io/github/license/Rystal-Team/Rystal-V6.svg?style=for-the-badge)](https://github.com/Rystal-Team/Rystal-V6/blob/main/LICENSE)
  [![Github Watchers](https://img.shields.io/github/watchers/Rystal-Team/Rystal-V6.svg?style=for-the-badge)](https://github.com/Rystal-Team/Rystal-V6)

</div>

## Key Features

- **Video Metadata**: Retrieve detailed metadata for YouTube videos, including title, duration, views, thumbnails, and more.
- **Captions**: Fetch and process captions (subtitles) for YouTube videos.
- **YouTube Search**: Perform YouTube searches and fetch metadata for the top results.

## Installation

Install Meta-YT using pip:

```bash
pip install meta-yt
```

## Usage

Here is a quick guide on how to use the library.

### Importing Necessary Modules

```python
from meta_yt import YouTube, Video, Caption
```

### Initializing the YouTube Object

You can initialize the `YouTube` object either with a search query or a video URL.

#### Using a Search Query

```python
yt = YouTube("cat videos")
print(yt.video.title)
```

#### Using a Video URL

```python
yt = YouTube("https://www.youtube.com/watch?v=dQw4w9WgXcQ", isUrl=True)
print(yt.video.title)
```

### Fetching Captions

You can fetch captions for a video and convert them to SubRip (SRT) format.

```python
captions = yt.video.get_captions(include_generated=True)
for lang, caption in captions.items():
    print(f"Captions in {lang}:")
    for line in caption.transcript:
        print(f"{line['start']} - {line['end']}: {line['text']}")
```

Since this library does not include a function to download or decrypt video streams, you will need to use external libraries such as YTDL or PyTube for those purposes.

## API Reference

### `class YouTube`

Represents a YouTube video and provides metadata fetching functionality.

#### `__init__(self, query: str, isUrl: bool = None)`

Initializes a YouTube object.

**Args:**
- `query` (str): The search query or video URL.
- `isUrl` (bool, optional): Whether the query is a URL. Defaults to `None`.

### `class Video`

Represents a YouTube video and provides methods to fetch metadata and captions.

#### `__init__(self, videoId: str)`

Initializes a Video object.

**Args:**
- `videoId` (str): The ID of the YouTube video.

#### Attributes

- `url`: The URL of the YouTube video.
- `title`: The title of the video.
- `channel`: The channel name of the video.
- `duration`: The duration of the video.
- `views`: The number of views on the video.
- `thumbnail`: The URL of the video thumbnail.
- `channel_url`: The URL of the video channel.
- `metadata`: Additional metadata fetched from the YouTube API.

#### `get_captions(self, include_generated: bool = False) -> dict`

Fetches the captions for the video.

**Args:**
- `include_generated` (bool, optional): Whether to include auto-generated captions. Defaults to `False`.

**Returns:**
- `dict`: A dictionary of `Caption` objects.

### `class Caption`

Represents captions for a YouTube video.

#### `__init__(self, baseUrl: str, language_code: str)`

Initializes a Caption object.

**Args:**
- `baseUrl` (str): The base URL of the video.
- `language_code` (str): The ISO 639-1 language code of the captions.

#### Attributes

- `url`: The URL for fetching captions.
- `language_code`: The ISO 639-1 language code of the captions.
- `language`: The language name of the captions.
- `transcript`: A list containing dictionaries representing each line of the transcript.

#### `to_srt(self) -> str`

Converts the transcript to SubRip (SRT) format.

**Returns:**
- `str`: The transcript in SubRip (SRT) format.

## Contributing

We welcome contributions! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.