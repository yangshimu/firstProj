
import math


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


lst = [13, -3, -25, 20, -3, -16, -23, 18, -12, -8, 50, 20, -7, 12, -5, -22, 15, -4, 7]
low, high, maxsum = find_max_subarray(lst, 0, len(lst)-1)
print(low, high, maxsum)

