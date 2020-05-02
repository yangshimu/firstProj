class Solution:
    def numDecodings(self, s: str) -> int:
        # for i in range(1,27):
        #     dic[i] = chr(i+64)
        memo = [-1]*len(s)
        return self.recursiveHelp(s, 0, memo)

    def recursiveHelp(self, s, indx, memo):
        if indx < len(s) and s[indx] == '0': return 0
        if indx < len(s) - 1 and s[indx:indx + 2] in ['30', '40', '50', '60', '70', '80', '90']:
            return 0
        if memo[indx]!=-1: return memo[indx]
        if indx == len(s) - 1:
            if s[indx] == '0':
                return 0
            else:
                return 1
        elif indx == len(s) - 2:
            if s[indx:] == '10' or s[indx:] == '20':
                return 1
            elif s[indx:] > '26':
                return 1
            else:
                return 2
        else:
            if s[indx:indx + 2] == '10' or s[indx:indx + 2] == '20':
                temp = self.recursiveHelp(s, indx + 2, memo)
                memo[indx]=temp
                return temp
            elif s[indx:indx + 2] > '26':
                # return self.recursiveHelp(s, indx + 1, memo)
                temp = self.recursiveHelp(s, indx + 1, memo)
                memo[indx] = temp
                return temp
            else:
                # return self.recursiveHelp(s, indx + 1, memo) + self.recursiveHelp(s, indx + 2, memo)
                temp1 = self.recursiveHelp(s, indx + 1, memo)
                temp2 = self.recursiveHelp(s, indx + 2, memo)
                memo[indx] = temp1+temp2
                return temp1+temp2


sot = Solution()
s = "9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"
print(sot.numDecodings(s))