class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for num in coins:
            for i in range(num, amount+1):
                dp[i] += dp[i-num]
        return dp[amount]