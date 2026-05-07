class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = float("inf")
        end = float("-inf")
        max_len = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if max_len < r-l+1:
                    start = l
                    end = r
                    max_len = r-l+1
                l -= 1
                r += 1

            l2, r2 = i, i+1
            while l2 >= 0 and r2 < len(s) and s[l2] == s[r2]:
                if max_len < r2-l2+1:
                    start = l2
                    end = r2

                    max_len = r2-l2+1
                l2 -= 1
                r2 += 1

        return s[start:end+1]