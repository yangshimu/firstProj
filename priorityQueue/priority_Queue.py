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


def max_queue(que):
    return que[0]


def extract_max_queue(que):
    size = len(que)
    maxValue = que[0]
    que[0], que[size-1] = que[size-1], que[0]
    max_heapify(que, size-1, 0)
    return maxValue


def increase_key_queue(que, idx, key):
    assert key >= que[idx]
    size = len(que)
    que[idx]=key
    idx_parent = parent(idx)
    while idx_parent >= 0 and que[idx_parent] < key:
        que[idx], que[idx_parent] = que[idx_parent], que[idx]
        idx = idx_parent
        idx_parent = parent(idx)


def insert_queue(que, key):
    que.append(float('-inf'))
    size = len(que)
    increase_key_queue(que, size-1, key)


array = [78, -66, 34, 245, -9, 120, -234, 0, 3, 567, 34, 39, -66]
# array = [random.randint(-100, 100) for _ in range(15)]
print(array)
build_max_heap(array)
print(array)
print(max_queue(array))
print(array)
# print(extract_max_queue(array))
# print(array)

increase_key_queue(array, 9, 250)

print(array)

insert_queue(array, -1)

print(array)

