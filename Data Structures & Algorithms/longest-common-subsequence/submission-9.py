class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        m, n = len(text1), len(text2)
        def traverse(i, j):
            if i == m or j == n:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            res = 0
            if text1[i] == text2[j]:
                res = 1 + traverse(i+1, j+1)
            else:
                res = max(traverse(i+1, j), traverse(i, j+1))
            dp[(i, j)] = res
            return res
        return traverse(0, 0)