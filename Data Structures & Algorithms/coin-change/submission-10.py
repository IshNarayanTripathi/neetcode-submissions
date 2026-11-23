class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def tra(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            if amount in dp:
                return dp[amount]
            res = float("inf")
            for coin in coins:
                res = min(res, 1+tra(amount-coin))
            dp[amount] = res
            return dp[amount]
        ans = tra(amount)
        return ans if ans != float("inf") else -1