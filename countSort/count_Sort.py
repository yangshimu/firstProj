import random


def count_sort(arA, arB, k):
    arC = [0 for _ in range(k+1)]
    n = len(arA)
    for j in range(n):
        arC[arA[j]] = arC[arA[j]] + 1
    for i in range(1, k+1):
        arC[i] = arC[i] + arC[i-1]
    for j in range(n-1, -1, -1):
        arB[arC[arA[j]]-1] = arA[j]
        arC[arA[j]] -= 1


n = 20
A = [random.randint(0, 100) for _ in range(n)]
B = [0 for _ in range(n)]
print(A)
k = max(A)
count_sort(A, B, k)
print(B)

