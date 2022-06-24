# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    # TODO: тело, которое вы реализовали на практической работе
    pass


# TODO: your code here
print("Самый короткий отрезок:", ...)  # Выводим название отрезка, например “АС”.




def distance(xa, ya, xb, yb):
    segment_length = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5
    return segment_length


print('Введите координаты трёх точек по оси Х и Y')

xa = int(input('Введите координату Х первой точки '))
ya = int(input('Введите координату Y первой точки '))

xb = int(input('Введите координату Х второй точки '))
yb = int(input('Введите координату Y второй точки '))

xc = int(input('Введите координату Х третьей точки '))
yc = int(input('Введите координату У третьей точки '))

AB = distance(xa, ya, xb, yb)
BC = distance(xb, yb, xc, yc)
AC = distance(xa, ya, xc, yc)
print('Отрезок АВ = ', AB)
print('Отрезок BC = ', BC)
print('Отрезок AC = ', AC)

if AB < BC and AB < AC:
    print('Самый короткий отрезок AB: ', AB)
if BC < AB and BC < AC:
    print('Самый короткий отрезок BC: ', BC)
if AC < AB and AC < BC:
    print('Самый короткий отрезок AC: ', AC)
if AC == BC or AC == AB:
    print('Самый короткий отрезок: ', AC)
    if BC == AB:
        print('Самый короткий отрезок: ', BC)
