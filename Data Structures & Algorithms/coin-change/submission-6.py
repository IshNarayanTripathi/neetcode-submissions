class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            if amount in dp:
                return dp[amount]
            min_coins = float("inf")
            for coin in coins:
                min_coins = min(min_coins, (1+dfs(amount-coin)))
            dp[amount] = min_coins
            return dp[amount]
        min_coins = dfs(amount)
        return min_coins if min_coins != float("inf") else -1


            