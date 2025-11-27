from lab03.text1 import normalize, tokenize, count_freq, top_n

def text_stats(text: str):
    norm = normalize(text)
    tokens = tokenize(norm)
    freq = count_freq(tokens)
    
    print(f'Всего слов: {len(tokens)}')# Длина списка tokens = 3
    print(f'Уникальных слов: {len(freq)}')#Количество уникальных слов в словаре freq
    print('Топ-5:')
    
    top = top_n(freq, 5)  # Берём 5 самых частых слов из словаря freq 
    for key, value in top:
        print(f"{key}: {value}") #Для каждой пары (слово, количество) в списке top печатаем слово и его количество
print('Привет, мир! Привет!!!')
text_stats('Привет, мир! Привет!!!')