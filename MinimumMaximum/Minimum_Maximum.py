import random


def min_max(ar):
    n = len(ar)
    if n % 2 == 0:
        if ar[0] < ar[1]:
            min_v = ar[0]
            max_v = ar[1]
        else:
            min_v = ar[1]
            max_v = ar[0]
        for i in range(2, n-1, 2):
            if ar[i] < ar[i+1]:
                if ar[i] < min_v:
                    min_v = ar[i]
                if ar[i+1] > max_v:
                    max_v = ar[i+1]
            else:
                if ar[i+1] < min_v:
                    min_v = ar[i+1]
                if ar[i] > max_v:
                    max_v = ar[i]
    else:
        min_v = max_v = ar[0]
        for i in range(1, n-1, 2):
            if ar[i] < ar[i+1]:
                if ar[i] < min_v:
                    min_v = ar[i]
                if ar[i+1] > max_v:
                    max_v = ar[i+1]
            else:
                if ar[i+1] < min_v:
                    min_v = ar[i+1]
                if ar[i] > max_v:
                    max_v = ar[i]
    return min_v, max_v


ar = [random.randint(-100, 100) for _ in range(20)]
print(ar)
print(min_max(ar))

