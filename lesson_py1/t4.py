# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

amt = 0
try:
    amt = int(input("Input number "))
except ValueError:
    print("Not an integer")
    quit()

res = amt / 6
if res.is_integer():
    res = int(res)
    pet = res
    ser = res
    kat = (pet + ser) * 2
    print(f"Катя — {kat}, Петя — {pet}, Серёжа — {ser}")
else:
    print("Cannot be divided into integer")