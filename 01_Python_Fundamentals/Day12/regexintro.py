import re

def find_words_starting_with_a(text):
    pattern = r"\ba\w*"
    return re.findall(pattern, text, flags=re.IGNORECASE)

def has_digits(text):
    return bool(re.search(r"\d", text))