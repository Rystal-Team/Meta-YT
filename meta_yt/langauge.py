# Dictionary mapping language codes to language names
from typing import Optional

language_code = {
    "af"     : "Afrikaans",
    "ar"     : "Arabic",
    "az"     : "Azerbaijani",
    "be"     : "Belarusian",
    "bg"     : "Bulgarian",
    "bn"     : "Bengali",
    "bs"     : "Bosnian",
    "ca"     : "Catalan",
    "cs"     : "Czech",
    "da"     : "Danish",
    "de"     : "German",
    "el"     : "Greek",
    "en"     : "English",
    "es"     : "Spanish",
    "et"     : "Estonian",
    "eu"     : "Basque",
    "fa"     : "Persian",
    "fi"     : "Finnish",
    "fr"     : "French",
    "ga"     : "Irish",
    "gl"     : "Galician",
    "gu"     : "Gujarati",
    "he"     : "Hebrew",
    "hi"     : "Hindi",
    "hr"     : "Croatian",
    "hu"     : "Hungarian",
    "hy"     : "Armenian",
    "id"     : "Indonesian",
    "is"     : "Icelandic",
    "it"     : "Italian",
    "ja"     : "Japanese",
    "ka"     : "Georgian",
    "kk"     : "Kazakh",
    "km"     : "Khmer",
    "kn"     : "Kannada",
    "ko"     : "Korean",
    "ky"     : "Kyrgyz",
    "lo"     : "Lao",
    "lt"     : "Lithuanian",
    "lv"     : "Latvian",
    "mk"     : "Macedonian",
    "ml"     : "Malayalam",
    "mn"     : "Mongolian",
    "mr"     : "Marathi",
    "ms"     : "Malay",
    "my"     : "Burmese",
    "ne"     : "Nepali",
    "nl"     : "Dutch",
    "no"     : "Norwegian",
    "pa"     : "Punjabi",
    "pl"     : "Polish",
    "pt"     : "Portuguese",
    "ro"     : "Romanian",
    "ru"     : "Russian",
    "si"     : "Sinhala",
    "sk"     : "Slovak",
    "sl"     : "Slovenian",
    "sq"     : "Albanian",
    "sr"     : "Serbian",
    "sv"     : "Swedish",
    "sw"     : "Swahili",
    "ta"     : "Tamil",
    "te"     : "Telugu",
    "th"     : "Thai",
    "tr"     : "Turkish",
    "uk"     : "Ukrainian",
    "ur"     : "Urdu",
    "uz"     : "Uzbek",
    "vi"     : "Vietnamese",
    "zh-Hans": "Chinese (Simplified)",
    "zh-Hant": "Chinese (Traditional)",
    "zu"     : "Zulu"
}


def get_language(code: str) -> Optional[str]:
    """
    Retrieve the language name based on the provided language code.

    Args:
        code (str): The language code for which the language name is to be retrieved.

    Returns:
        Optional[str]: The language name corresponding to the provided code, or None if not found.
    """
    return language_code.get(code)
