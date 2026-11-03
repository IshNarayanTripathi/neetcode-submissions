class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        max_dist = 0
        n = len(s)
        for i in range(n):
            l1, r1 = i, i
            while l1 >= 0 and r1 <= n-1 and s[l1] == s[r1]:
                l1 -= 1
                r1 += 1
            l2, r2 = i, i+1
            while l2 >= 0 and r2 <= n-1 and s[l2] == s[r2]:
                l2 -= 1
                r2 += 1
            dist1 = r1-l1-1
            dist2 = r2-l2-1
            if dist1 >= dist2 and dist1 > max_dist:
                start = l1+1
                end = r1-1
                max_dist = dist1
            elif dist2 > dist1 and dist2 > max_dist:
                start = l2+1
                end = r2-1
                max_dist = dist2
        return s[start:end+1]

