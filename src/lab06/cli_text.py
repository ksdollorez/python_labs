import argparse
from pathlib import Path
import re
from collections import Counter

def normalize(text):
    """Нормализация текста"""
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def tokenize(text):
    """Разделение на слова"""
    return re.findall(r'\b[a-zа-яё0-9]+\b', text, re.IGNORECASE)

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


def main():
    # создание объекта парсера с описанием программы
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")

    subparsers = parser.add_subparsers(dest="command", help="Доступные команды", required=True)

    # Сначала создаем парсер для stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов в тексте")
    stats_parser.add_argument("--input", required=True, help="Входной текстовый файл")
    stats_parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Количество топовых слов (по умолчанию: 5)",
    )
    
    # Затем создаем парсер для cat
    cat_parser = subparsers.add_parser("cat", help="Вывод содержимого файла")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    args = parser.parse_args()

    # Проверяем команду и обрабатываем соответствующие аргументы
    if args.command == "cat":
        file = Path(args.input)
        if not file.exists():
            parser.error(f"Файл '{args.input}' не найден")
        
        # реализация команды cat
        with open(file, "r", encoding="utf-8") as f:
            number = 1
            for row in f:
                row = row.rstrip("\n")
                if args.n:  # если указан флаг n -> печатаем пронумерованные строки
                    print(f"{number}: {row}")
                    number += 1
                else:
                    print(row)

    elif args.command == "stats":
        file = Path(args.input)
        if not file.exists():
            parser.error(f"Файл '{args.input}' не найден")
        
        # реализация команды stats
        with open(file, "r", encoding="utf-8") as f:
            data = f.read()
        
        # Нормализуем текст
        normalized = normalize(data)
        # Токенизируем
        tokens = tokenize(normalized)
        # Считаем частоту
        freq = count_freq(tokens)
        # Получаем топ слов
        top = top_n(freq, n=args.top)

        # выводим топ слов
        print(f"Топ {args.top} слов:")
        for i, (word, count) in enumerate(top, 1):
            print(f"{i}. {word} - {count}")


if __name__ == "__main__":
    main()