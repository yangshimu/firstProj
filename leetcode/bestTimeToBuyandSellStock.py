class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        helper = [0]*length
        for i in range(1, length):
            helper[i] = prices[i] - prices[i - 1]
        for i in range(1, length - 1):
            if helper[i] > 0:
                helper[i + 1] += helper[i]
        maxV = max(helper[1:])
        if maxV > 0:
            return maxV
        else:
            return 0


p = [1,2]
sot = Solution()

print(sot.maxProfit(p))