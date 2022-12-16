#Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве

import math

xa = float(input("Введите x1 точки A: "))
ya = float(input("Введите y1 точки A: "))
xb = float(input("Введите x2 точки B: "))
yb = float(input("Введите y2 точки B: "))
num = (xb-xa)**2+(yb-ya)**2
sqrt = math.sqrt(num)
print(str(sqrt))

