# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
# были повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть

import random

def oryol_or_reshka():
    x = random.randint(0, 1)
    return x

n = int(input("Введите количество n монеток: "))
print()

oryol = 0
reshka = 0
for i in range(n):
    x = oryol_or_reshka()
    # print(x) # проверка
    if x == 0:
        oryol += 1
    else:
        reshka += 1

if reshka > oryol:
    print(oryol)
else:
    print(reshka)