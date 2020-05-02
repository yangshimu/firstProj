
import random
import math
import time


def find_max_crossing_subarray(lst, left, mid, right):
    left_sum = float("-inf")
    sum_accum = 0
    for i in range(mid, left-1, -1):
        sum_accum += lst[i]
        if sum_accum > left_sum:
            left_sum = sum_accum
            left_low = i
    right_sum = float("-inf")
    sum_accum = 0
    for i in range(mid+1, right+1):
        sum_accum += lst[i]
        if sum_accum > right_sum:
            right_sum = sum_accum
            right_high = i
    return left_low, right_high, right_sum+left_sum


def find_max_subarray(lst, low, high):
    if low == high:
        return low, high, lst[low]
    else:
        mid = math.floor((low + high)/2)
        left_low, left_high, left_sum = find_max_subarray(lst, low, mid)
        right_low, right_high, right_sum = find_max_subarray(lst, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(lst, low, mid, high)
        if left_sum > right_sum and left_sum > cross_sum:
            return left_low, left_high, left_sum
        elif right_sum > left_sum and right_sum > cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def find_max_subarray2(lst):
    n = len(lst)
    cur_low = cur_high = 0
    cur_sum = lst[0]
    end_low = end_high = 0
    end_sum = lst[0]
    for i in range(1, n):
        if end_sum > 0:
            end_high = i
            end_sum += lst[i]
        else:
            end_low = end_high = i
            end_sum = lst[i]
        if end_sum > cur_sum:
            cur_low = end_low
            cur_high = end_high
            cur_sum = end_sum
    return cur_low, cur_high, cur_sum


size = 1000000
lst_rand = [random.randint(-100, 100) for _ in range(size)]
start = time.time()
low, high, maxsum = find_max_subarray(lst_rand, 0, size-1)
print(low, high, maxsum)
print(time.time() - start)

start = time.time()
low, high, maxsum = find_max_subarray2(lst_rand)
print(low, high, maxsum)
print(time.time() - start)
# lst = [13, -3, -25, 20, -3, -16, -23, 18, -12, -8, 50, 20, -7, 12, -5, -22, 15, -4, 7]

