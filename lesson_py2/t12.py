# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных
# числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого
# Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

import random, time

def nat_num():
    x = random.randint(1, 1000)
    return x

x = nat_num()
y = nat_num()
# x = 1000 # проверка оптимизации
# y = 1000 # проверка оптимизации
sum = x + y
pro = x * y

# print(f"Подсказки: сумма — {sum}, произведение — {pro}")
# print(f"Ответ: x — {x}, y — {y}") # Проверка

iter = 0
flag = False
i = 0
k = 0
j = 0
x1 = 0
y1 = 0
start = time.time()
while i < sum:
    if flag:
        break
    while k < sum:
        if flag:
            break
        while j < sum:
            # print(f"Загрузка: {i} — {j} — {sum} — {pro} — {i * j} — {iter}") # проверка оптимизации
            iter += 1
            if i + j == sum and i * j == pro:
                flag = True
                x1 = i
                y1 = j
            if flag:
                stop = time.time()
                break
            j += 1
            k += 1
        j = 0
    k = 0
    i += 1

print(f"Загаданные числа Пети: {x}, {y}") # Проверка
print(f"Подсказки от Пети: сумма — {sum}, произведение — {pro}")
print(f"Итераций — {iter}, время в сек.: {stop - start}") # проверка оптимизации
if flag:
    print(f"Ответ Кати: {x1}, {y1}")