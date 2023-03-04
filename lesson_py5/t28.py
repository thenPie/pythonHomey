# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются
# только +1 и -1. Также нельзя использовать циклы.

def sum(a, b):
    if b == 0:
        return a
    return sum(a, b - 1) + 1

fir, sec = [int(x) for x in input("Enter two values: ").split()]

print(sum(fir, sec))