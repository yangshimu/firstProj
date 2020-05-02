class Solution:

    def permute(self, nums):
        res = []
        self.helper(nums, 0, res)
        return res

    def helper(self, nums, begin, res):
        if begin == len(nums):
            temp = [e for e in nums]
            res.append(temp)
        else:
            for i in range(begin, len(nums)):
                nums[i], nums[begin] = nums[begin], nums[i]
                self.helper(nums, begin + 1, res)
                nums[i], nums[begin] = nums[begin], nums[i]


sol = Solution()
print(sol.permute([1, 2, 3]))

