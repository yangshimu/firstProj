import random


def minimum(ar):
    minValue = ar[0]
    n = len(ar)
    for i in range(1, n):
        if minValue > ar[i]:
            minValue = ar[i]
    return minValue


ar = [random.randint(-100, 200) for _ in range(20)]
print(ar)
print(minimum(ar))

