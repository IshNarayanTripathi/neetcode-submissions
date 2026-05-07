class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            left_val = s[left].lower()
            right_val = s[right].lower()
            if left_val != right_val:
                return False
            left += 1
            right -= 1
        return True

        
