
import math
import numpy
import random


def parent(idx):
    return math.ceil(idx/2)-1


def left_child(idx):
    return idx*2+1


def right_child(idx):
    return idx*2+2


def max_heapify(arra, size, idx):
    left = left_child(idx)
    right = right_child(idx)
    if left < size and arra[idx] < arra[left]:
        largest = left
    else:
        largest = idx
    if right < size and arra[largest] < arra[right]:
        largest = right
    if idx != largest:
        arra[idx], arra[largest] = arra[largest], arra[idx]
        max_heapify(arra, size, largest)


def build_max_heap(arra):
    n = len(arra)
    m = math.floor(n/2)
    for i in range(m-1, -1, -1):
        max_heapify(arra, n, i)


def heap_sort(arra):
    n = len(arra)
    build_max_heap(arra)
    for i in range(n-1, 0, -1):
        arra[0], arra[i] = arra[i], arra[0]
        max_heapify(arra, i, 0)


# array = [78, -66, 34, 245, -9, 120, -234, 0, 3, 567, 34, 39, -66]
array = [random.randint(-100, 100) for _ in range(15)]
print(array)
heap_sort(array)
print(array)





