class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                skipl = s[left+1:right+1]
                skipr = s[left:right]
                return skipl == skipl[::-1] or skipr == skipr[::-1]
            left+=1
            right-=1
        return True
