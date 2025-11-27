def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not text:
        return ""
    
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    
    if casefold:
        text = text.casefold()
    
    control_chars = '\t\n\r\v\f'
    for char in control_chars:
        text = text.replace(char, ' ')
    
    text = ' '.join(text.split())
    
    return text
import re

def tokenize(text: str) -> list[str]:
    if not text:
        return []
    
    pattern = r'\b[\w]+(?:-[\w]+)*\b'
    tokens = re.findall(pattern, text)
    
    return tokens
from collections import Counter

def count_freq(tokens: list[str]) -> dict[str, int]:
    return dict(Counter(tokens))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if not freq:
        return []
    
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    return sorted_items[:n]