# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here

import random
numbers = []

print ('Введите количество чисел в списке ')
n = int(input ())
count = 1


while count <= n:
    numbers.append (random.randint(-100, 100))
    count +=1
print ("Ваш список: ", numbers)
count = 1
summ = 0
positive_even_numbers=[]
for b in numbers:
#    print (b, end=" ")
    if b > 0 and b % 2 == 0:
        positive_even_numbers.append(b)
        #print ("Положительные чётные числа: ", b)
        summ = summ + b
print ("Положительные чётные числа: ",
       positive_even_numbers)
print ("Cумма этих чисел: ", summ)
