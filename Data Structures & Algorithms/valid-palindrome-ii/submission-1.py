class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            new_str = s[:i]+s[i+1:]
            if self.ispalin(new_str):
                return True
        return False

    def ispalin(self, s):
        left, right = 0, len(s)-1
        while left <= right:
            if s[left] !=  s[right]:
                return False
            left += 1
            right -= 1
        return True