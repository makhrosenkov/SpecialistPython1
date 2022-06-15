# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр", "Святослав", "Святослав"]
name_length = []
print("Динные имена: ", names)
count = 0
the_longest = 0
for b in names:
    name_length = len(b)
    if name_length > count:
        the_longest = name_length
        count = the_longest
        name = b
print("Но самое длинное:", name)
