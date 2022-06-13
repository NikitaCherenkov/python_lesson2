# Реализуйте алгоритм перемешивания списка.

import random

numbers = 10
rand = random.Random()
list_input = []
for i in range(0, numbers):
    list_input.append(round(rand.random(), 2))
print('Входной список:', list_input)
list_random = []
temp = 0
while len(list_random) < numbers:
    temp = rand.randint(0, numbers - 1)
    if temp not in list_random:
        list_random.append(temp)
list_output = []
for i in range(0, numbers):
    list_output.append(list_input[list_random[i]])
print('Выходной список:', list_output)
