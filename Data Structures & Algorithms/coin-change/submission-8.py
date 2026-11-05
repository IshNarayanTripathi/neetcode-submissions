class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        n = len(coins)
        def memo(amount):
            if amount == 0:
                return 0
            elif amount < 0:
                return float("inf")
            elif amount in dp:
                return dp[amount]
            res = float("inf")
            for i in range(n):
                res = min(res, 1+memo(amount-coins[i]))
            dp[amount] = res
            return dp[amount]
        ans = memo(amount) 
        return ans if ans != float("inf") else -1           