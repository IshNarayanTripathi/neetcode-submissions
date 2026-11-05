class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        for i in range(amount+1):
            res = float("inf")
            for j in coins:
                if j > i:
                    continue
                res = min(res, 1+dp[i-j])
            dp[i] = min(dp[i], res)
        return dp[amount] if dp[amount] != float("inf") else -1