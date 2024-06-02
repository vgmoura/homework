def print_params(a=1, b='string', c=True): # Создаем фуенкцию со значениями по умолчанию
    print(a, b, c)

print_params()
print_params(a=1, b='string')
print_params(a=1)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 'apple', False]
values_dict = {'a': 1, 'b': 'string', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32,"'Строка'"]

print_params(*values_list_2,42)