
def left_boundary(nums, target):
    left = 0
    right = len(nums)
    while left<right:
        mid = left + (right-left)//2
        if nums[mid]<target:
            left = mid+1
        elif nums[mid]>target:
            right = mid
        elif nums[mid]==target:
            right = mid

    if right == len(nums): return -1
    return right if nums[right]==target else -1


def last_less_than(nums, target):
    left = 0
    right = len(nums)
    while left<right:
        mid = left + (right-left)//2
        if nums[mid]<target:
            left = mid+1
        elif nums[mid]>target:
            right = mid
        elif nums[mid]==target:
            right = mid

    # if right == len(nums): return -1
    return right-1


def right_boundary(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left)//2
        if nums[mid]<target:
            left = mid+1
        elif nums[mid]==target:
            left = mid+1
        else:
            right = mid

    if left==0: return -1
    return left-1 if nums[left-1]==target else -1


def first_large_than(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left)//2
        if nums[mid]<target:
            left = mid+1
        elif nums[mid]==target:
            left = mid+1
        else:
            right = mid

    if left==len(nums): return -1
    return left

arr = [-1, 1, 2, 3, 3, 3, 5, 8, 12, 12, 235]
print(left_boundary(arr, 2352))
print(right_boundary(arr, 6))
print(last_less_than(arr, 12))
print(first_large_than(arr,-1))
