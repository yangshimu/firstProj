class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        i = j = 0
        ans = 0
        while True:
            while i + 1 < length and prices[i] >= prices[i + 1]:
                i += 1
            if i >= length - 1: break
            j = i + 1
            while j + 1 < length and prices[j] <= prices[j + 1]:
                j += 1

            ans += prices[j] - prices[i]
            i = j + 1
            # if i >= length - 1: break
        return ans



sot = Solution()
p = [1,2,3,4,5]
print(sot.maxProfit(p))