
def get_matrix(n, m, value): # Объявление функции с параметрами
    matrix = []  # Создание пустого списка
    for _ in range(n):  # Внешний цикл для создания строк
        row = []  # Создание пустого списка для каждой строки
        for _ in range(m):  # Внутренний цикл для создания столбцов
            row.append(value)  # Добавление значения в строку
        matrix.append(row)  # Добавление строки в матрицу
    return matrix  # Возвращение готовой матрицы

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Вывод результатов
print(result1)
print(result2)
print(result3)