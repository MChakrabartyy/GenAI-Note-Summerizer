 # utils.py

import re

def clean_text(text):
    """Basic cleanup: remove extra whitespace + line breaks"""
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\s{2,}', ' ', text)
    return text.strip()
