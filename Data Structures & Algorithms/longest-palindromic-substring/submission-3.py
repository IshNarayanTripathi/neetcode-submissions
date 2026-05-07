class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s[0]
        longest_palin = ""
        length = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    if length < j - i + 1:
                        longest_palin = s[i:j+1]
                        length = j - i + 1
        return longest_palin

    def isPali(self, s, i, j):
        left, right = i, j
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
