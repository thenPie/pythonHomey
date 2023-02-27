import secrets
length = int(input("Введите количество элементов в массиве: "))
search = int(input("Введите число для поиска: "))
list = []
for i in range(length):
    number = int(secrets.randbelow(10))
    list.append(number)
isthere = 0
for k in list:
    if k == search:
        isthere += 1
if isthere > 0:
    print(f"Число {search} появлялось в массиве {isthere} раз(а)")
print(list)