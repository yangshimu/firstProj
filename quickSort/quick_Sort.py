
import random


def partition(arra, p, r):
    pivot = arra[r]
    i = p - 1
    for j in range(p, r):
        if arra[j] <= pivot:
            i += 1
            arra[i], arra[j] = arra[j], arra[i]
    arra[i+1], arra[r] = arra[r], arra[i+1]
    return i+1


def quick_sort(arra, p, r):
    if p < r:
        q = partition(arra, p, r)
        quick_sort(arra, p, q-1)
        quick_sort(arra, q+1, r)


# array = [78, -66, 34, 245, -9, 120, -234, 0, 3, 567, 34, 39, -66]
array = [random.randint(-300, 300) for _ in range(30)]
print(array)
quick_sort(array, 0, len(array)-1)
print(array)


def random_partition(ar, p, r):
    i = random.randint(p, r)
    ar[i], ar[r] = ar[r], ar[i]
    return partition(ar, p, r)


def random_quick_sort(ar, p, r):
    if p < r:
        q = random_partition(ar, p, r)
        random_quick_sort(ar, p, q-1)
        random_quick_sort(ar, q+1, r)


array = [random.randint(-300, 300) for _ in range(30)]
print(array)
random_quick_sort(array, 0, len(array)-1)
print(array)

