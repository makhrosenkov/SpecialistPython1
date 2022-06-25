# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

a = ...
b = ...

def palindrome(number):
    number = str(number)
    return number == number[::-1]


# print(palindrome(112311))
# print(palindrome('adf'))

a = 1
b = 100
i = 0
while a <= b:
    if palindrome(a):
        i = i + 1
    a = a + 1
print(i)
