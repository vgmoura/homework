def is_prime(number): #функция: проверка на простое число
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5 + 1)): #проверка, что выбранное число не делиться ни на что в диапазоне от 2 до этого числа
        if number % i == 0:
            return False
    else:
        return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = [number for number in numbers if is_prime(number)]
not_primes = [number for number in numbers if not is_prime(number)]
not_primes.remove(1)

print("Primes:", primes)
print("Not primes:", not_primes)
