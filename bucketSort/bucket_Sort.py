import random
import math


def insert_sort(seq):
    n = len(seq)
    for j in range(1, n):
        key = seq[j]
        i = j-1
        while i >= 0 and seq[i] > key:
            seq[i+1] = seq[i]
            i = i-1
        seq[i+1] = key


def bucket_sort(lst):
    n = len(lst)
    buckets = [[] for _ in range(n)]
    for ele in lst:
        buckets[math.floor(n*ele)].append(ele)
    for i in range(n):
        insert_sort(buckets[i])
    lst = [ele for bucket in buckets for ele in bucket]
    return lst


lst = [random.uniform(0, 1) for _ in range(20)]
print(lst)
lst = bucket_sort(lst)
print(lst)

