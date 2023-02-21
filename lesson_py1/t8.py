# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

hor = 0
ver = 0
chu_orig = 0

try:
    hor, ver, chu_orig = int(input("Введите размер шоколадки (горизонтально x вертикально), отломленные дольки k; через Enter: ")), int(input()), int(input())
except (ValueError, TypeError):
    print("Not an integer or not enough values")
    quit()
print()

# print chocolote full size
chunk_amt1 = 0
print("Chocolate")
i = 0
k = 0
while i < ver:
    while k < hor:
        print(end = "O ")
        k += 1
        chunk_amt1 += 1
    k = 0
    print()
    i += 1
chunk_amt2 = chunk_amt1
print()

checker = False

# разлом по вертикали
chunk_amt1 -= ver # разлом тут
if chu_orig != chunk_amt1:
    hor_side = 1
    while hor_side < hor:
        if chu_orig == chunk_amt1:
            checker = True
        chunk_amt1 -= ver
        hor_side += 1
elif chu_orig == chunk_amt1:
    checker = True

# разлом по горизонтали
chunk_amt2 -= hor # разлом тут
if chu_orig != chunk_amt2:
    ver_side = 1
    while ver_side < ver:
        if chu_orig == chunk_amt2:
            checker = True
        chunk_amt2 -= hor
        ver_side += 1
elif chu_orig == chunk_amt2:
    checker = True

if checker == True:
    print("yes, possible")
elif checker == False:
    print("no, not possible")