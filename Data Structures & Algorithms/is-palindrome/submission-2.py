class Solution:
    def isPalindrome(self, s: str) -> bool:
        for val in s:
            if not val.isalnum():
                s = s.replace(val, '')
        s = s.lower()
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

        
