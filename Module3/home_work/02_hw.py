# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
# TODO: your code here

print ('Введите количес тво чисел в списке')
n = int(input ())
count = 1

while count <= n:
    numbers.append (random.randint(-100, 100))
    count +=1
print ("Ваш список: ", numbers)
