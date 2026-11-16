# ПЗ № 5, Вариант 1, Задача 1


def sum_digits(n):
    # Считаем сумму цифр числа
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def count_steps(n):
    # Считаем, сколько раз нужно вычесть сумму цифр до нуля
    steps = 0
    while n > 0:
        n -= sum_digits(n)
        steps += 1
    return steps


while True:
    try:
        num = int(input("Введите целое число (>= 0): "))
        if num >= 0:
            break
        print("Число должно быть не меньше 0!")
    except ValueError:
        print("Неправильно ввели! Нужно целое число.")

print("Нуль получится через", count_steps(num), "действий.")