TN_MAP = {
    "2101": "кофе и цикорий",
    "21011": "кофе растворимый",
    "2106": "сухие смеси",
    "2201": "вода",
    "2202": "безалкогольные напитки",
    "2203": "пиво",
    "2204": "вино",
    "2206": "сброженные напитки",
    "2208": "крепкий алкоголь",
    "0901": "кофе",
    "0902": "чай",
}

def classify_tnved(code):
    if not code:
        return None

    code = str(code)

    best = ""
    best_val = None

    for k, v in TN_MAP.items():
        if code.startswith(k) and len(k) > len(best):
            best = k
            best_val = v

    return best_val
