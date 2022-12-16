# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).


x = int(input("Введите координату Х не равную 0 : "))
y = int(input("Введите координату Y не равную 0 : "))

if x != 0 and y != 0:
    if x > 0 and y > 0:
        print(f"Точка {x, y} находится в 1 плоскости")
    elif x < 0 and y > 0:
            print(f"Точка {x, y} находится во 2 плоскости")
    elif x < 0 and y < 0:
            print(f"Точка {x, y} находится в 3 плоскости")
    elif x > 0 and y < 0:
            print(f"Точка {x, y} находится в 4 плоскости")

