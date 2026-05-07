class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    count += 1
        return count

    def isPali(self, s, i, j):
        left, right = i, j
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
