class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(remain):
            if remain == 0:
                return 0
            if remain < 0:
                return float("inf")
            if remain in dp:
                return dp[remain]
            min_coin = float("inf")
            for coin in coins:
                res = dfs(remain-coin)
                if res != float("inf"):
                    min_coin = min(min_coin, 1+res)
            dp[remain] = min_coin
            return dp[remain]
        min_coin = dfs(amount)
        return min_coin if min_coin != float("inf") else -1