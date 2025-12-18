# tests/test_json_csv.py
import json
import csv
import os
import tempfile
import pytest

# ФУНКЦИИ ПРЯМО ЗДЕСЬ - НИКАКИХ ИМПОРТОВ!
def json_to_csv(src_path: str, dst_path: str):
    """Конвертирует JSON файл в CSV"""
    if not os.path.exists(src_path):
        raise FileNotFoundError(f"Файл не найден: {src_path}")
    
    try:
        with open(src_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise ValueError(f"Некорректный JSON в файле: {src_path}")
    
    if not data:
        raise ValueError("JSON файл пустой")
    
    if isinstance(data, list) and len(data) > 0:
        fieldnames = data[0].keys()
    else:
        raise ValueError("Некорректная структура JSON")
    
    with open(dst_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def csv_to_json(src_path: str, dst_path: str):
    """Конвертирует CSV файл в JSON"""
    if not os.path.exists(src_path):
        raise FileNotFoundError(f"Файл не найден: {src_path}")
    
    with open(src_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    
    if not data:
        raise ValueError("CSV файл пустой")
    
    with open(dst_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ТЕСТЫ
def test_json_to_csv_basic():
    """Тест преобразования JSON в CSV"""
    # Создаем временный JSON
    json_data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30}
    ]
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as json_file:
        json.dump(json_data, json_file)
        json_path = json_file.name
    
    csv_path = json_path.replace('.json', '.csv')
    
    try:
        json_to_csv(json_path, csv_path)
        
        # Проверяем CSV
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        
        assert len(rows) == 2
        assert rows[0]['name'] == 'Alice'
        assert rows[0]['age'] == '25'
        assert rows[1]['name'] == 'Bob'
        assert rows[1]['age'] == '30'
    finally:
        # Удаляем временные файлы
        if os.path.exists(json_path):
            os.remove(json_path)
        if os.path.exists(csv_path):
            os.remove(csv_path)

def test_csv_to_json_basic():
    """Тест преобразования CSV в JSON"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['name', 'age'])
        writer.writeheader()
        writer.writerow({"name": "Alice", "age": 25})
        writer.writerow({"name": "Bob", "age": 30})
        csv_path = csv_file.name
    
    json_path = csv_path.replace('.csv', '.json')
    
    try:
        csv_to_json(csv_path, json_path)
        
        # Проверяем JSON
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        assert len(data) == 2
        assert data[0]['name'] == 'Alice'
        assert data[0]['age'] == '25'
        assert data[1]['name'] == 'Bob'
        assert data[1]['age'] == '30'
    finally:
        if os.path.exists(csv_path):
            os.remove(csv_path)
        if os.path.exists(json_path):
            os.remove(json_path)

def test_json_to_csv_empty_file():
    """Тест на пустой JSON файл"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write('')
        json_path = f.name
    
    csv_path = json_path.replace('.json', '.csv')
    
    try:
        # Меняем текст ошибки на тот, который реально вызывается
        with pytest.raises(ValueError, match="Некорректный JSON в файле"):
            json_to_csv(json_path, csv_path)
    finally:
        if os.path.exists(json_path):
            os.remove(json_path)

def test_file_not_found():
    """Тест на несуществующий файл"""
    with pytest.raises(FileNotFoundError):
        json_to_csv("nonexistent_file_12345.json", "output.csv")

def test_invalid_json():
    """Тест на некорректный JSON"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write('{invalid json}')
        json_path = f.name
    
    csv_path = json_path.replace('.json', '.csv')
    
    try:
        with pytest.raises(ValueError):
            json_to_csv(json_path, csv_path)
    finally:
        if os.path.exists(json_path):
            os.remove(json_path)