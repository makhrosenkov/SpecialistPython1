# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(tiket_number):
    # TODO: your code here
    tiket_number = str(tiket_number)
    numbers_of_tiket_number = list(tiket_number)
    summ1 = 0
    summ2 = 0
    max_lenght = 6
    if len(numbers_of_tiket_number) != max_lenght:
        return False
    for number in numbers_of_tiket_number[0:3]:
        number = int(number)
        summ1 = summ1 + number
        # print(summ1)

    for number1 in numbers_of_tiket_number[3:7]:
        number1 = int(number1)
        summ2 = summ2 + number1
        # print(summ2)

    if summ1 == summ2:
        return True

    # Тестируем функцию


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(436751134))
print(lucky_ticket(4367513244253))
print(lucky_ticket(4))
print(lucky_ticket(111111))
