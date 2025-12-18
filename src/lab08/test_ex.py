import os
import sys
import json

# Добавляем текущую директорию в путь для импорта
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Импортируем из текущей директории
from models import Student

# Создаем упрощенные версии функций сериализации прямо здесь
def students_to_json(students, path):
    """Сохранение списка студентов в JSON файл."""
    data = [s.to_dict() for s in students]
    
    # Создаем директорию, если она не существует
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def students_from_json(path) -> list[Student]:
    """Загрузка студентов из JSON файла."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except FileNotFoundError:
        return []
    
    result = []
    for d in raw:
        try:
            result.append(Student.from_dict(d))
        except ValueError:
            continue
    
    return result

def main():
    print("Тест класса Student")
    
    # Создаем первого студента
    print("Студент создан")
    student1 = Student(
        fio="Иванов Иван Иванович",
        birthdate="2007-04-25",
        group="БИВТ-25-01",
        gpa=4.5
    )
    print(student1)
    print(f'Возраст: {student1.age()} лет')
    print(f'словарь:{student1.to_dict()}')
    print()
    
    # Проверка валидации
    print("Проверка валидации")
    try:
        Student('Тест', "2020-13-45", "БИВТ-25-01", 3.0)
    except ValueError as e:
        print(f"Произошла ошибка валидации даты: {e}")

    try:
        Student("Тест", "2020-01-01", "БИВТ-25-02", 6)
    except ValueError as e:
        print(f"Произошла ошибка валидации GPA: {e}")
    print()
    
    # Проверка сериализации
    print("Проверка сериализации")
    
    # Создаем абсолютные пути
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    
    # Создаем папку data/lab08
    data_dir = os.path.join(project_root, "data", "lab08")
    os.makedirs(data_dir, exist_ok=True)
    
    # Создаем полные пути к файлам
    output_file = os.path.join(data_dir, "students_output.json")
    input_file = os.path.join(data_dir, "students_input.json")
    
    # Создаем список студентов для сохранения
    students = [
        Student("Иванов Иван Иванович", "2007-04-25", "БИВТ-25-01", 4.5),
        Student("Петров Пётр Петрович", "2007-04-05", "БИВТ-25-02", 3.8),
    ]
    
    # Сохраняем студентов
    students_to_json(students, output_file)
    print("Студенты сохранены в students_output.json")
    
    # Создаем входной файл, если его нет
    if not os.path.exists(input_file):
        # Создаем пример входного файла с 3 вариантом
        example_students = [
            Student("Сидоров Алексей Петрович", "2006-03-22", "БИВТ-23-3", 4.1),
            Student("Иванов Иван", "2007-07-10", "БИВТ-25-01", 4.0)
        ]
        students_to_json(example_students, input_file)
    
    # Загружаем студентов из входного файла
    loaded_students = students_from_json(input_file)
    print("Студенты загружены из students_input.json")
    
    # Выводим загруженных студентов
    for student in loaded_students:
        print(f"  - {student}")

if __name__ == "__main__":
    main()