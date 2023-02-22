# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = 0

try:
    n = int(input("Введите число: "))
except ValueError:
    print("Not an integer")
    quit()

i = 1
while i <= n:
    print(i)
    i *= 2