import re

def clean_text(text):
    """
    Clean text by removing special characters and converting to lowercase.
    """

    text = text.lower()

    # Remove URLs
    text = re.sub(r'http\S+', '', text)

    # Remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    return text
