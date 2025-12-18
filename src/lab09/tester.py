from group import Group
from models import Student


def print_students(title, students):
    print("\n" + title)
    for s in students:
        print(f"{s.fio} | {s.birthdate} | {s.group} | {s.gpa}")


g = Group("data/lab09/students.csv")

print_students("Изначальный CSV:", g.list())

new_st = Student("Холецкий Богдан", "2004-02-22", "БИВТ-22-01", 4.7)
g.add(new_st)
print_students("После добавления:", g.list())

found = g.find("ив")  # ищем по подстроке
print_students("Поиск 'ив':", found)

g.update("Петров Петр", gpa=4.1, group="БИВТ-21-5")
print_students("После обновления данных Петрова:", g.list())

g.remove("Суров Миша")
print_students("После удаления Сурова:", g.list())