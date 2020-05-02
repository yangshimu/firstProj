
class Solution:

    def groupAnagrams(self, strs):
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return list(d.values())



sol = Solution()
str= ["eat", "tea", "tan", "ate", "nat", "bat"]
print(sol.groupAnagrams(str))
