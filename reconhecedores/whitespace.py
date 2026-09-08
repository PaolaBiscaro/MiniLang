import re

def identify_and_ignore_whitespace(word: str) -> bool:
    WHITESPACES = (r'[ \t\r\n]+')
    return re.fullmatch(WHITESPACES, word) is not None
