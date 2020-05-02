class Solution:
    def plusOne(self, digits):
        length = len(digits)
        temp = digits[length - 1]
        carry = (temp + 1) // 10
        digits[length - 1] = (temp + 1) % 10
        i = length - 2
        while i >= 0 and carry == 1:
            temp = digits[i]
            digits[i] = (temp + carry) % 10
            carry = (temp + carry) // 10

            i -= 1
        if i == -1 and carry == 1:
            digits.insert(0, 1)
        return digits


sol = Solution()
dig= [9,7,9,9]
print(sol.plusOne(dig))