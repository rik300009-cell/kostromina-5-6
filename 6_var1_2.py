# ПЗ № 6, Вариант 1, Задача 2
import random

while True:
    try:
        n = int(input("Введите размер списка N: "))
        if n > 0:
            break
        print("Размер должен быть больше 0!")
    except ValueError:
        print("Неправильно ввели! Нужно целое число.")

# Заполняем список случайными числами
a = []
for i in range(n):
    a.append(random.randint(-20, 20))

# Ищем номера элементов, которые больше правого соседа
res = []
for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        res.append(i + 1)

print("Исходный список:", a)
print("Номера элементов больше правого соседа:", res)
print("Количество таких элементов:", len(res))