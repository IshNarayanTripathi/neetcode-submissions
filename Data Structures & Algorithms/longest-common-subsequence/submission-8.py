class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            max_len = float("-inf")
            if text1[i] == text2[j]:
                max_len = 1+dfs(i+1, j+1)
            else:
                max_len = max(dfs(i+1, j), dfs(i, j+1))
            dp[(i, j)] = max_len
            return dp[(i, j)]
        return dfs(0, 0)