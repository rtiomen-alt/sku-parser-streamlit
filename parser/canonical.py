import re

def build_canonical(text: str):
    if not isinstance(text, str):
        return None

    t = text.lower()

    t = re.sub(r"\d+(\.\d+)?\s?(л|ml|мл|кг|g)?", "", t)
    t = t.replace("со вкусом", "")
    t = re.sub(r"\s+", " ", t).strip()

    return t
