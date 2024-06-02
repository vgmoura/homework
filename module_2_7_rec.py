# Рекурсивное умножение цифр

def get_multiplied_digits(number):
    str_number = str(number)

# Определяем первую цифру в числе
    if len(str_number) < 2:
        return int(str_number[:1])

    first = int(str_number[:1]) # записываем первый символ в переменную
    return first * get_multiplied_digits(int(str_number[1:])) # умножаем первую цифру на результат функции


result = get_multiplied_digits(40203)
print(result)

result = get_multiplied_digits(203)
print(result)

result = get_multiplied_digits(3)
print(result)