#Напишите программу, которая принимает на вход число N
#и выдает набор произведений чисел от 1 до N в виде списка.#
#1 = 1 * 1, 2 = 1 * 2, 3 = 1 * 2 * 3, 4 = 1 * 2 * 3 * 4 и т.д.
#- 4 -> [1, 2, 6, 24]


N = int(input(""))
sp = []
m = 1
for i in range(1, N+1):
    if i > 0:
        m = i * m
    sp.append(m)
print(sp)
