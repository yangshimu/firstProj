class Solution:
    def largestRectangleArea(self, heights):
        if len(heights) == 0:
            return 0
        return self.getMaxArea(heights, 0, len(heights) - 1)

    def getMaxArea(self, heights, left, right):
        if left == right:
            return heights[left]
        mid = (right + left) // 2
        leftArea = self.getMaxArea(heights, left, mid)
        rightArea = self.getMaxArea(heights, mid + 1, right)
        midArea = self.getMidArea(heights, mid, left, right)
        return max(leftArea, rightArea, midArea)

    def getMidArea(self, heights, mid, left, right):
        i = mid
        j = mid + 1
        minH = min(heights[i:j + 1])
        area = 2 * minH
        while i >= left and j <= right:
            minH = min(minH, heights[i], heights[j])
            area = max(area, minH * (j - i+1))
            if i == left:
                j += 1
            elif j == right:
                i -= 1
            elif heights[i - 1] >= heights[j + 1]:
                i -= 1
            else:
                j += 1
        return area

sot = Solution()
nums = [1,2,3,4,5]
print(sot.largestRectangleArea(nums))