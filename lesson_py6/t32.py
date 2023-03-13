import random

arr = [random.randint(-9, 9), random.randint(-9, 9), random.randint(-9, 9), random.randint(-9, 9), random.randint(-9, 9), random.randint(-9, 9), random.randint(-9, 9), random.randint(-9, 9), random.randint(-9, 9), random.randint(-9, 9)]
print(arr)
minNum = int(input())
maxNum = int(input())
for i in range(len(arr)):
    if minNum <= arr[i] <= maxNum:
        print(i)