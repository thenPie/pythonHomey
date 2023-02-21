# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних
# трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая
# проверяет счастливость билета.

inp = input("Input six digit ticket number: ")

if inp.isdigit():
    if len(inp) == 6:
        if int(inp[0]) + int(inp[1]) + int(inp[2]) == int(inp[3]) + int(inp[4]) + int(inp[5]):
            print("`Tis a lucky ticket!")
        else:
            print("A regular ticket number")
    else:
        print("Not a six digit number")
else:
    print("Is not an integer")