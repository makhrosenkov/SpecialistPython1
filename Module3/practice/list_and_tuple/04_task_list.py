# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here

import random

print('Введите количество чисел в списке')
n = int(input())
numbers = []
summ = 0

for _ in range(n):
    numbers.append(random.randint(-10, 10))
for number in numbers:
    if number > 0:
        summ = summ + number
print(numbers)
print(summ)
