def clean_text(text):
    # PEP8: 4 espacios por indentación, no tabs
    if not text:
        return ""
    return text.strip().lower()
