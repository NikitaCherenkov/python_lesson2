# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('Введите n: '))
list = []
for i in range(1, n + 1):
    list.append((1+1/i)**i)
print('Сумма:', round(sum(list), 4))
