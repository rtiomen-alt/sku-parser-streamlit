def extract_flavor(text: str):
    if not isinstance(text, str):
        return None

    t = text.lower()

    if "манго" in t and "маракуйя" in t:
        return "tropical"
    if "лимон" in t:
        return "citrus"
    if "апельсин" in t:
        return "citrus"

    return "unknown"
