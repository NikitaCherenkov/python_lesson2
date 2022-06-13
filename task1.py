# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

N = int(input("Введите число N: "))
product_list = []
if N > 0:
    product_list.append(1)
if N > 1:
    product_list.append(2)
for i in range(1, N - 1):
    product_list.append((i + 2) * product_list[i])
print(product_list)
