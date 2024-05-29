def single_root_words(root_word, *other_word): # Функция с параметрами
    same_words = []  # Создаем пустой список внутри функции
    for n in other_words:
        if root_word.lower() in n.lower() or n.lower() in root_word.lower(): # Подбираем подходящие слова
            same_words.append(n)  # Добавляем слово в результирующий список, при выполнении условия
    return same_words  # Возвращаем образованный функцией список

root_word = "rich"
other_words = ["rich", "richest", "orichalcum", "cheers", "rechies"]
result1 = single_root_words(root_word, *other_words)
print(result1)  # Вывод: ['rich', 'richest', 'orichalcum']

root_word = "Able"
other_words = ['Disablement', 'Able', 'Mable', 'Disable', 'Bagel']
result2 = single_root_words(root_word, *other_words)
print(result2) # Вывод: ['Disablement', 'Able', 'Mable', 'Disable']