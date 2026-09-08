import re

def identify_and_ignores_line_comment(word: str):
    LINE_COMMENT = re.compile(r"//[^\r\n]*")
    if LINE_COMMENT.fullmatch(word):
        return True
    return None