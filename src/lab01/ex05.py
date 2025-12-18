fio = str(input("ФИО: "))
name = fio.split()
initials = [word[0].upper() for word in name]
print("Инициалы: ", "".join(initials) + ".")
print("Длина (символов): ", len(" ".join(name)))
