# Дано целое число.
# Если оно делится на 3 без остатка - вывести "Foo",
# если делится на 5 - вывести "Bar",
# а если делится на 3 и на 5 - вывести "Foobar".
# Для всех остальных случаев не выводить ничего.

# TODO: your code here


print ('Введите целое число: ')
integer = int(input())
foo = 3
bar = 5

if integer % foo == 0 and integer % bar == 0:
    print ('foobar')
else:
    if integer % foo == 0:
        print ('foo')
    if integer % bar == 0:
        print ('bar')
