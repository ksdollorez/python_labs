def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, tuple):
        return TypeError
    if len(rec)!=3:
        raise ValueError
    if type(rec[2]) is not float:
        raise TypeError
    if len(rec[1])==0:
        raise ValueError
    if not isinstance(rec[0], str):
        return TypeError
    name_parts=rec[0].strip().split()
    if len(name_parts)==3:
        m1, m2, m3 = name_parts
        return f"{m1.capitalize()} {m2[0].upper()}.{m3[0].upper()}., гр. {rec[1].upper()}, GPA {rec[2]:.2f}"
    elif len(name_parts)==2:
        m1, m2 = name_parts
        return f"{m1.capitalize()} {m2[0].upper()}., гр. {rec[1].upper()}, GPA {rec[2]:.2f}"
    else:
        raise ValueError
print('tuples')
print("(\"Иванов Иван Иванович\", \"BIVT-25\", 4.6) ->", format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print("(\"Петров Пётр\", \"IKBO-12\", 5.0) ->", format_record(("Петров Пётр", "IKBO-12", 5.0)))
print("(\" сидорова анна сергеевна \", \"ABB-01\", 3.999) ->", format_record((" сидорова анна сергеевна ", "ABB-01", 3.999)))