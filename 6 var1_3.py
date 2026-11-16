# ПЗ № 6, Вариант 1, Задача 3
import random

while True:
    try:
        n = int(input("Введите размер списка N (N >= 4): "))
        if n >= 4:
            break
        print("N должно быть не меньше 4!")
    except ValueError:
        print("Неправильно ввели! Нужно целое число.")

while True:
    try:
        k = int(input(f"Введите K (1 < K < {n - 1}): "))
        l = int(input(f"Введите L ({k} < L < {n}): "))
        if 1 < k < l < n:
            break
        print(f"Нужно, чтобы выполнялось 1 < K < L < {n}!")
    except ValueError:
        print("Неправильно ввели! Нужны целые числа.")

# Генерируем исходный список
a = []
for i in range(n):
    a.append(random.randint(1, 50))

print("Исходный список:", a)

# Переворачиваем элементы строго между K-м и L-м (нумерация с 1)
a[k:l - 1] = a[k:l - 1][::-1]

print("Результирующий список:", a)