class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        max_len = 1
        res = s[0]
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPali(s[i:j+1]):   # FIXED: include j
                    if (j - i + 1) > max_len:   # FIXED: consistent length
                        max_len = j - i + 1
                        res = s[i:j+1]          # FIXED: include j
        return res

    def isPali(self, s):
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
