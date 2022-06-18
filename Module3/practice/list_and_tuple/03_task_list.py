# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

# TODO: your code here

numbers1 = []
summ = 0
number = 0
for _ in range(n):
    numbers1.append(random.randint(-100, 100))
for number in numbers1:
    summ = summ + number
print(numbers1)
print(summ)
