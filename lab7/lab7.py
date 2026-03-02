# ===============================
# ЛАБОРАТОРНАЯ РАБОТА
# Тема: Разработка функций и рекурсивных алгоритмов
# ===============================


# ===============================
# Задание 1. Функции и параметры
# ===============================

def add(a, b):
    return a + b


def power(a, n=2):
    return a ** n


def sum_all(*args):
    total = 0
    for value in args:
        total += value
    return total


# ===============================
# Задание 2. Область видимости
# ===============================

counter = 10

def change_value():
    global counter
    counter = 20


# ===============================
# Задание 3. Факториал
# ===============================

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# ===============================
# Задание 4. Рекурсивная сумма цифр
# ===============================

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)


# ===============================
# Задание 5. Рекурсивный максимум
# ===============================

def max_element(arr, index=0):
    if index == len(arr) - 1:
        return arr[index]

    max_rest = max_element(arr, index + 1)

    if arr[index] > max_rest:
        return arr[index]
    else:
        return max_rest


# ===============================
# Дополнительно: Фибоначчи
# ===============================

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_fast(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# ===============================
# Практические задачи
# ===============================

def average(a, b, c):
    return (a + b + c) / 3


def is_even(n):
    return n % 2 == 0


def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)


def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


def fast_power(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        half = fast_power(a, n // 2)
        return half * half
    else:
        return a * fast_power(a, n - 1)


def count_depth(n):
    if n == 0:
        return 1
    return 1 + count_depth(n - 1)


# ===============================
# Примеры запуска
# ===============================

if __name__ == "__main__":

    print("add(3, 5) =", add(3, 5))
    print("power(4) =", power(4))
    print("sum_all(1,2,3,4) =", sum_all(1, 2, 3, 4))

    print("\nГлобальная переменная до:", counter)
    change_value()
    print("После изменения:", counter)

    print("\nФакториал (рекурсия) 5 =", factorial_recursive(5))
    print("Факториал (итерация) 5 =", factorial_iterative(5))

    print("\nСумма цифр 1234 =", sum_digits(1234))

    print("Максимум [3,8,2,10,5] =", max_element([3, 8, 2, 10, 5]))

    print("\nФибоначчи 6 (рекурсия) =", fibonacci(6))
    print("Фибоначчи 6 (быстро) =", fibonacci_fast(6))

    print("\nСреднее (3,6,9) =", average(3, 6, 9))
    print("Чётное ли 10? =", is_even(10))

    print("\nЧисла от 5 до 1:")
    print_numbers(5)

    print("\nПалиндром 'level' =", is_palindrome("level"))

    print("Быстрое возведение 2^10 =", fast_power(2, 10))

    print("Глубина рекурсии для 5 =", count_depth(5))