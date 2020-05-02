

def findMid(nums1, nums2):


    def recur(nums1, l1, r1, nums2, l2, r2):

        mid1 = l1 + (r1-l1)//2
        mid2 = l2 + (r2-l2)//2
        offset = ((r1-l1+1)&1)^1
        if l1>=r1:
            return min(nums1[l1], nums2[l2])
        if nums1[mid1]<nums2[mid2]:
            return recur(nums1, mid1+offset, r1, nums2, l2, mid2)
        elif nums1[mid1]>nums2[mid2]:
            return recur(nums1, l1, mid1, mid2+offset, r2)
        else:
            return nums1[mid1]

    return recur(nums1, 0, len(nums1)-1, nums2, 0, len(nums2))


a1 = [1,2,3,4,6]
a2 = [15,16,17,18,20]

print(findMid(a1, a2))

