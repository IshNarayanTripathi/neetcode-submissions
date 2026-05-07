class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            new1 = s[:i]+s[i+1:]
            if new1 == new1[::-1]:
                return True
        return False