def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, tuple): # проверка, что это кортеж
        return TypeError
    if len(rec)!=3: # в кортеже ровно 3 элемента
        raise ValueError
    if type(rec[2]) is not float: #Проверяем, что GPA - это число с плавающей точкой (float)
        raise TypeError
    if len(rec[1])==0: #номер группы не пустая строка
        raise ValueError
    if not isinstance(rec[0], str): #ФИО - это строка
        return TypeError
    name_parts=rec[0].strip().split()#убираем лишние пробелы в начале и конце, разбиваем строку на части по пробелам
    if len(name_parts)==3:
        m1, m2, m3 = name_parts
        return f"{m1.capitalize()} {m2[0].upper()}.{m3[0].upper()}., гр. {rec[1].upper()}, GPA {rec[2]:.2f}" # первые буквы фио заглавные, остальные маленькие
    # группа заглавными, GPA с двумя знаками после запятой
    elif len(name_parts)==2: #без отчества
        m1, m2 = name_parts
        return f"{m1.capitalize()} {m2[0].upper()}., гр. {rec[1].upper()}, GPA {rec[2]:.2f}"
    else:
        raise ValueError
print('tuples')
print("(\"Иванов Иван Иванович\", \"BIVT-25\", 4.6) ->", format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print("(\"Петров Пётр\", \"IKBO-12\", 5.0) ->", format_record(("Петров Пётр", "IKBO-12", 5.0)))
print("(\" сидорова анна сергеевна \", \"ABB-01\", 3.999) ->", format_record((" сидорова анна сергеевна ", "ABB-01", 3.999)))