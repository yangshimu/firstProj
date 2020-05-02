import math
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


# def quick_sort(arra, p, r):
#     if p < r:
#         q = partition(arra, p, r)
#         quick_sort(arra, p, q-1)
#         quick_sort(arra, q+1, r)
#
#
# # array = [78, -66, 34, 245, -9, 120, -234, 0, 3, 567, 34, 39, -66]
# array = [random.randint(-300, 300) for _ in range(30)]
# print(array)
# quick_sort(array, 0, len(array)-1)
# print(array)


def random_partition(ar, p, r):
    i = random.randint(p, r)
    ar[i], ar[r] = ar[r], ar[i]
    return partition(ar, p, r)


def randomized_select(ar, p, r, i):
    if p == r:
        return ar[p]
    q = random_partition(ar, p, r)
    k = q-p+1
    if k == i:
        return ar[q]
    elif k > i:
        return randomized_select(ar, p, q-1, i)
    else:
        return randomized_select(ar, q+1, r, i-k)


# ar = [random.randint(-100, 100) for _ in range(20)]
# # ar = [23, -9]
# print(ar)
# print(randomized_select(ar, 0, len(ar)-1, 2))


def insert_sort(seq):
    n = len(seq)
    for j in range(1, n):
        key = seq[j]
        i = j-1
        while i >= 0 and seq[i] > key:
            seq[i+1] = seq[i]
            i = i-1
        seq[i+1] = key


def partition_specify(arra, p, r, pivot):
    # pivot = arra[r]
    i = p - 1
    for j in range(p, r+1):
        if arra[j] <= pivot:
            i += 1
            arra[i], arra[j] = arra[j], arra[i]
    # arra[i+1], arra[r] = arra[r], arra[i+1]
    return i


# Intro to Algo. 9.3 Selection in worst-case linear time, python code


def select(ar, p, r, i):
    if p == r:
        return ar[p]
    n = r - p + 1
    m = math.floor(n/5)
    s = [ar[p+j*5:p+(j+1)*5] for j in range(m)]
    if ar[p+m*5:p+n]:
        s.append(ar[p+m*5:p+n])
    for sub_s in s:
        insert_sort(sub_s)
    medians = []
    for sub_s in s:
        medians.append(sub_s[math.floor((len(sub_s)+1)/2)-1])

    # 求各组中值组成的元组medians的中值
    x = select(medians, 0, len(medians)-1, math.floor((len(medians)+1)/2))
    q = partition_specify(ar, p, r, x)
    k = q-p+1
    if i == k:
        return x
    elif i < k:
        '''
        这里q位置上的元素不一定是x, 有可能是其它值(partition和partition_specify不同的地方)，
        为防止漏掉某些元素，这里子问题是p到q，而不是p到q-1。
        '''
        return select(ar, p, q, i)
    else:
        return select(ar, q+1, r, i-k)


ar = [-346, -16, 0, 312, -6, 55, 12, -90]
print(select(ar, 0, len(ar)-1, 3))

