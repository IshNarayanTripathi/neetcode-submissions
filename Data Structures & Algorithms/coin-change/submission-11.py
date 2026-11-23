class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for s in range(coin, amount+1):
                dp[s] = min(dp[s], 1+dp[s-coin])
        return dp[amount] if dp[amount] != float("inf") else -1