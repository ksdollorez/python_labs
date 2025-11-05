from text import normalize, tokenize, count_freq, top_n

def text_stats(text: str):
    norm = normalize(text)
    tokens = tokenize(norm)
    freq = count_freq(tokens)
    
    print(f'Всего слов: {len(tokens)}')
    print(f'Уникальных слов: {len(freq)}')
    print('Топ-5:')
    
    top = top_n(freq, 5)  # Предполагается, что top_n принимает второй параметр - количество
    for key, value in top:
        print(f"{key}: {value}")
print('Привет, мир! Привет!!!')
text_stats('Привет, мир! Привет!!!')