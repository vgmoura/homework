def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = [num for num in numbers if is_prime(num)]
not_primes = [num for num in numbers if not is_prime(num)]
not_primes.remove(1)

print("Простые числа:", primes)
print("Не простые числа:", not_primes)