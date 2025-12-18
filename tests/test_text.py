# tests/test_text.py
import pytest


# Функции прямо здесь, без импорта
def normalize(text: str) -> str:
    """Приводит текст к нижнему регистру и убирает лишние пробелы."""
    if not text:
        return ""
    text = text.lower()
    text = text.replace("ё", "е")
    text = " ".join(text.split())
    return text


def tokenize(text: str) -> list[str]:
    """Разбивает текст на слова (токены)."""
    if not text:
        return []
    import re

    words = re.findall(r"\b[\w\-]+\b", text, flags=re.UNICODE)
    return words


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Считает частоту слов."""
    from collections import Counter

    return dict(Counter(tokens))


def top_n(freq: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Возвращает N самых частых слов."""
    if not freq:
        return []
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]


# Твои тесты (оставляешь как есть)
@pytest.mark.parametrize(
    "src,expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize(src, expected):
    assert normalize(src) == expected


@pytest.mark.parametrize(
    "src,expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
    ],
)
def test_tokenize(src, expected):
    assert tokenize(src) == expected


def test_count_and_top():
    tokens = ["a", "b", "a", "c", "b", "a"]
    freq = count_freq(tokens)
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]


def test_top_tie_breaker():
    freq = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert top_n(freq, 2) == [("aa", 2), ("bb", 2)]


def test_dop():
    assert normalize("") == ""
    assert tokenize("") == []
    assert count_freq([]) == {}
    assert top_n({}, 5) == []


def test_top_dop():
    freq = {"a": 3, "b": 2}
    assert top_n(freq, 5) == [("a", 3), ("b", 2)]
