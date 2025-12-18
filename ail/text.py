import re
from collections import Counter


def normalize(text):
    """Нормализация текста"""
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def tokenize(text):
    """Разделение на слова"""
    return re.findall(r"\b[a-zа-яё0-9]+\b", text, re.IGNORECASE)


def count_freq(words):
    """Подсчет частоты"""
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def top_n(freq, n=5):
    """Топ N слов"""
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
