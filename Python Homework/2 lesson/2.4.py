#Напишите программу, которая принимает на вход 2 числа.
#Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
#Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

import math

N = int(input())
pos_1 = int(input())
pos_2 = int(input())
pr = []
p1 = pos_1 - 1
p2 = pos_2 - 1
m = 0
z = list(range(-N, N+1))
for i in z:
    if i == p1:
        m = z[p1]
        pr.append(m)
    if i == p2:
        m = i + m
        pr.append(m)
print(math.prod(pr))





















