class Solution:
    def subsets(self, nums):
        ans = []
        self.helper(nums, 0, [], ans)
        return ans

    def helper(self, nums, start, temp, ans):
        ans.append(list(temp))
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.helper(nums, i + 1, temp, ans)
            temp.pop()


sot =Solution()
inp = [4,1,0]
print(sot.subsets(inp))