
def findKth2(nums1, nums2, K):

    def recur(nums1, l1, r1, nums2, l2, r2, k):
        if l1>r1:
            return nums2[l2+k]
        if l2>r2:
            return nums1[l1+k]
        if k==0:
            return min(nums2[l2], nums1[l1])
        pos1 = l1 + k // 2 if (l1 + (k // 2)) < r1 else r1
        pos2 = l2 + k // 2 if (l2 + (k // 2)) < r2-l1 else r2
        if nums1[pos1]<nums2[pos2]:
            return recur(nums1, pos1+1, r1, nums2, l2, r2, k - k//2 - 1)
        elif nums1[pos1]>nums2[pos2]:
            return recur(nums1, l1, r1, nums2, pos2+1, r2, k - k // 2 - 1)
        else:
            return nums1[pos1]

    if not nums1: return nums2[K-1]
    if not nums2: return nums1[K-1]
    return recur(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, K-1)


a1=[1,2,3,4]
a2=[5,6,7,8]
print(findKth2(a1, a2, 8))