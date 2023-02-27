import secrets
length = int(input("Введите количество элементов в массиве: "))
search = int(input("Введите число для поиска: "))
list = []
for i in range(length):
    number = secrets.randbelow(10)
    while number == search:
        number = secrets.randbelow(10)
    list.append(number)
print(list)
print(f"Ближайшее число к искомому: {min(list, key = lambda x:abs(x-search))}")