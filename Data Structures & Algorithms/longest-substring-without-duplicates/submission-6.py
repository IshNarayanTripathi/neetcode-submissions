class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contains = dict()
        l = 0
        n = len(s)
        max_len = 0
        for r in range(n):
            while s[r] in contains:
                contains[s[l]] -= 1
                if contains[s[l]] == 0:
                    del contains[s[l]]
                l += 1
            contains[s[r]] = 1
            max_len = max(max_len, r-l+1)
        return max_len
