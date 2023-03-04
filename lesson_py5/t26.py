# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def square(a, s):
    if s == 1:
        return a
    elif s == 0:
        return 1
    return square(a, s - 1) * a

fir, sec = [int(x) for x in input("Enter two values: ").split()]

print(square(fir, sec))