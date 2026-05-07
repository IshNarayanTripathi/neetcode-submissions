class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        dp = {len(s):0}
        def dfs(ind):
            if ind in dp:
                return dp[ind]
            res = len(s)-ind
            res = 1+dfs(ind+1)
            for j in range(ind, len(s)):
                if s[ind:j+1] in words:
                    res = min(res, dfs(j+1))
            dp[ind] = res
            return dp[ind]
        return dfs(0)