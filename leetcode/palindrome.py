def isPalindrome(s):
    if not s: return True
    lower = s.lower()
    left = 0
    right = len(s) - 1
    while left < right:
        while left < len(s) and (ord(lower[left]) < 97 or ord(lower[left]) > 122):
            left += 1
        while right > -1 and (ord(lower[right]) < 97 or ord(lower[right]) > 122):
            right -= 1
        if lower[left] == lower[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))