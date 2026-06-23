import re

SEPARATORS = r",|;|\n|/"

def split_rows(text: str):
    if not isinstance(text, str):
        return []
    return [p.strip() for p in re.split(SEPARATORS, text) if p.strip()]
