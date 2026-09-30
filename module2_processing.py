import re
from collections import Counter

from module1_input import get_words


# =========================================================
# MODULE 2: TEXT PROCESSING & STATISTICS
# =========================================================

def analyze_text_data(text):

    words = get_words(text)

    # Basic statistics
    total_words = len(words)
    total_characters = len(text)

    # Sentences
    sentences = re.split(r"[.!?]+", text)
    sentences = [s for s in sentences if s.strip()]
    total_sentences = len(sentences)

    # Paragraphs
    paragraphs = re.split(r"\n\s*\n", text)
    paragraphs = [p for p in paragraphs if p.strip()]
    total_paragraphs = len(paragraphs)

    # Unique words
    unique_words = set(words)
    total_unique_words = len(unique_words)

    # Frequency
    frequency = Counter(words)

    return (
        words,
        total_words,
        total_characters,
        total_sentences,
        total_paragraphs,
        total_unique_words,
        frequency
    )