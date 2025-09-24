fio=str(input('ФИО: '))
name=fio.split()
symbols=[new for new in name if new]
initials=[word[0].upper() for word in symbols]
print('Инициалы: ',''.join(initials)+'.')
print('Длина (символов): ',len(' '.join(symbols)))
