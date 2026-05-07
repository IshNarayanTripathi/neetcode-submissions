class Solution:
    def countSubstrings(self, s: str) -> int:
        count = set()
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count.add((l, r))
                l -= 1
                r += 1
            l2, r2 = i, i+1
            while l2 >= 0 and r2 < len(s) and s[l2] == s[r2]:
                count.add((l2, r2))
                l2 -= 1
                r2 += 1
        return len(count)
            