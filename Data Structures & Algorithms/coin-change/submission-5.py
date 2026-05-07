class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(curr):
            if curr == 0:
                return 0
            if curr < 0:
                return float("inf")
            if curr in dp:
                return dp[curr]
            res = float("inf")
            for coin in coins:
                res = min(res, 1+dfs(curr-coin))
            dp[curr] = res
            return dp[curr]
        return dfs(amount) if dfs(amount) != float("inf") else -1