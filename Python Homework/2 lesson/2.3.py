#Задайте список из n чисел,
# заполненный по формуле (1 + 1/n) ** n
# и выведите на экран их сумму.


N = int(input(""))
sp = []
m = 1
for i in range(1, N+1):
    if i > 0:
        m = round((1+1/i) ** i, 3)
    sp.append(m)
print(sp, round(sum(sp), 3))
