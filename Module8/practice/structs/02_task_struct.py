# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию написанную на одном из прошлых занятий.
# Получите новый список, элементами которого будут:
#   1. неповторяющиеся(уникальные) элементы исходного списка:
#   например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
#   2. элементы исходного списка, которые не имеют повторений(встречаются только один раз):
#   например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]


def gen_list(size, of, to):
    import random
    numbers = []
    i = 0
    while i < size:
        number = random.randint(of, to)
        numbers.append(number)
        i = i + 1
    return numbers


numbers = gen_list(7, 1, 10)
print(numbers)
newnumbers = []
for number in numbers:
    if numbers.count(number) == 1:
        newnumbers.append(number)
print(newnumbers)
