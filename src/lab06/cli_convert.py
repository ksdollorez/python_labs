#!/usr/bin/env python3
"""
Конвертер данных CLI
Команды: json2csv, csv2json, csv2xlsx
"""

import argparse
from pathlib import Path
import sys
import json
import csv
import pandas as pd


def json_to_csv(input_file: str, output_file: str):
    """Конвертация JSON в CSV"""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Проверяем, что данные - список словарей
        if not isinstance(data, list):
            data = [data]
        
        if not data:
            raise ValueError("JSON файл пустой")
        
        # Получаем заголовки из первого элемента
        fieldnames = list(data[0].keys())
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        
        print(f"Конвертация завершена: {input_file} → {output_file}")
        
    except Exception as e:
        sys.stderr.write(f"Ошибка конвертации JSON→CSV: {e}\n")
        sys.exit(1)


def csv_to_json(input_file: str, output_file: str, indent: int = 2):
    """Конвертация CSV в JSON"""
    try:
        data = []
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=indent)
        
        print(f"Конвертация завершена: {input_file} → {output_file}")
        
    except Exception as e:
        sys.stderr.write(f"Ошибка конвертации CSV→JSON: {e}\n")
        sys.exit(1)


def csv_to_xlsx(input_file: str, output_file: str, sheet_name: str = "Sheet1"):
    """Конвертация CSV в XLSX"""
    try:
        df = pd.read_csv(input_file)
        df.to_excel(output_file, index=False, sheet_name=sheet_name)
        
        print(f"Конвертация завершена: {input_file} → {output_file}")
        
    except Exception as e:
        sys.stderr.write(f"Ошибка конвертации CSV→XLSX: {e}\n")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Конвертер JSON↔CSV, CSV→XLSX",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(
        dest="command",
        title="доступные команды",
        metavar=""
    )
    subparsers.required = True
    
    # Команда json2csv
    json2csv_parser = subparsers.add_parser(
        "json2csv",
        help="Конвертировать JSON в CSV",
        description="Преобразует JSON файл в CSV формат"
    )
    json2csv_parser.add_argument(
        "--in",
        dest="input",
        required=True,
        help="Путь к входному JSON"
    )
    json2csv_parser.add_argument(
        "--out",
        dest="output",
        required=True,
        help="Путь к выходному CSV"
    )
    
    # Команда csv2json
    csv2json_parser = subparsers.add_parser(
        "csv2json",
        help="Конвертировать CSV в JSON",
        description="Преобразует CSV файл в JSON формат"
    )
    csv2json_parser.add_argument(
        "--in",
        dest="input",
        required=True,
        help="Путь к входному CSV"
    )
    csv2json_parser.add_argument(
        "--out",
        dest="output",
        required=True,
        help="Путь к выходному JSON"
    )
    csv2json_parser.add_argument(
        "--indent",
        type=int,
        default=2,
        help="Отступ в JSON файле (по умолчанию: 2)"
    )
    
    # Команда csv2xlsx
    csv2xlsx_parser = subparsers.add_parser(
        "csv2xlsx",
        help="Конвертировать CSV в XLSX",
        description="Преобразует CSV файл в Excel формат"
    )
    csv2xlsx_parser.add_argument(
        "--in",
        dest="input",
        required=True,
        help="Путь к входному CSV"
    )
    csv2xlsx_parser.add_argument(
        "--out",
        dest="output",
        required=True,
        help="Путь к выходному XLSX"
    )
    csv2xlsx_parser.add_argument(
        "--sheet",
        default="Sheet1",
        help="Название листа в Excel (по умолчанию: Sheet1)"
    )
    
    args = parser.parse_args()
    
    # Проверяем существование входного файла
    if not Path(args.input).exists():
        sys.stderr.write(f"Ошибка: входной файл '{args.input}' не найден\n")
        sys.exit(1)
    
    # Выполняем соответствующую команду
    if args.command == "json2csv":
        json_to_csv(args.input, args.output)
    elif args.command == "csv2json":
        csv_to_json(args.input, args.output, getattr(args, 'indent', 2))
    elif args.command == "csv2xlsx":
        csv_to_xlsx(args.input, args.output, getattr(args, 'sheet', 'Sheet1'))


if __name__ == "__main__":
    main()