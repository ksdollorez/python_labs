import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    if Path(json_path).is_absolute():
        raise ValueError("путь к JSON должен быть относительным")
    if Path(csv_path).is_absolute():
        raise ValueError("путь к CSV должен быть относительным")
    
    if not json_path.lower().endswith('.json'):
        raise ValueError("нэ JSON")
    if not csv_path.lower().endswith('.csv'):
        raise ValueError("нэ CSV")
    
    if not Path(json_path).exists():
        raise FileNotFoundError(f"файл не найден: {json_path}")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if not data:
        raise ValueError("пустой JSON")
    if not isinstance(data, list):
        raise ValueError("JSON должен быть списком")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("все элементы должны быть словарями")
    
    fields = sorted(data[0].keys())
    
    Path(csv_path).parent.mkdir(parents=True, exist_ok=True)
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in data:
            complete_row = {field: str(row.get(field, '')) for field in fields}
            writer.writerow(complete_row)

def csv_to_json(csv_path: str, json_path: str) -> None:
    if not csv_path.lower().endswith('.csv'):
        raise ValueError("нэ CSV")
    if not json_path.lower().endswith('.json'):
        raise ValueError("нэ JSON")
    
    if not Path(csv_path).exists():
        raise FileNotFoundError(f"файл не найден: {csv_path}")
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        data = list(csv.DictReader(f))
    
    if not data:
        raise ValueError("пустой CSV")
    
    Path(json_path).parent.mkdir(parents=True, exist_ok=True)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    Path("data/out").mkdir(parents=True, exist_ok=True)
    
    json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
    csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")