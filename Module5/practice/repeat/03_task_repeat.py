# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

a = ...
b = ...


def palindrome(number):
    number = str(number)
    return number == number[::-1]


print(palindrome(112311))

a = 1
b = 100

while a <= b:
    if palindrome(a):
        print(a)
    a = a + 1
