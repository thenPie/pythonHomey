# Найдите сумму цифр трехзначного числа.

inp = input("Input three digit number: ")

if inp.isdigit():
    if len(inp) == 3:
        print(f"{inp[0]} + {inp[1]} + {inp[2]} = {int(inp[0]) + int(inp[1]) + int(inp[2])}")
    else:
        print("Not a three digit integer")
else:
    print("Is not an integer")