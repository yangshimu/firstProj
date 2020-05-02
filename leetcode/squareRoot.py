class Solution:
    def mySqrt(self, x):
        r = x
        while r*r - x>0.1 or r*r-x<-0.1:
            r = (r + x/r) / 2
        return int(r)


sot = Solution()
print(sot.mySqrt(10002))