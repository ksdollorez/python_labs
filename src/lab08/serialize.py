import json
import os
from .models import Student

def students_to_json(students, path):
    """Сохранение списка студентов в JSON файл."""
    data = [s.to_dict() for s in students]
    
    # Создаем директорию, если она не существует
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"Студенты сохранены в {path}")

def students_from_json(path) -> list[Student]:
    """Загрузка студентов из JSON файла."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except FileNotFoundError:
        print(f"Файл {path} не найден")
        return []
    
    result = []
    for d in raw:
        try:
            result.append(Student.from_dict(d))
        except ValueError as e:
            print(f"Ошибка при создании студента: {e}")
    
    print(f"Студенты загружены из {path}")
    return result