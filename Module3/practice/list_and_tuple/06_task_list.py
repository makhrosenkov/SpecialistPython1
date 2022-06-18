# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число
numbers = []
multiples_of_three = []

summ = 0
if first_number <= second_number:

     while first_number <= second_number:
          numbers.append(first_number)
          if first_number % 3 == 0:
               multiples_of_three.append(first_number)

          first_number = first_number + 1

     #i += i
elif second_number <= first_number:
     while second_number <= first_number:
          numbers.append(second_number)
          second_number=second_number+1
          if second_number % 3 == 0:
               multiples_of_three.append(second_number)
          #print (numbers)

print (numbers)
print("кратные трём: ", multiples_of_three)
