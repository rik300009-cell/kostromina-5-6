# ПЗ № 5, Вариант 1, Задача 2


def power_a234(a):
    # Вычисляем 2-ю, 3-ю и 4-ю степень числа a
    b = a ** 2
    c = a ** 3
    d = a ** 4
    return b, c, d


for i in range(1, 6):
    while True:
        try:
            a = float(input(f"Введите {i}-е число: "))
            break
        except ValueError:
            print("Неправильно ввели! Введите число.")

    b, c, d = power_a234(a)
    print(f"Число {a}: B={b}, C={c}, D={d}")