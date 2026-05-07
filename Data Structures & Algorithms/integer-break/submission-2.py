class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        def dfs(num):
            if num in dp:
                return dp[num]
            max_prod = 0
            for i in range(1, num):
                max_prod = max(max_prod, i*(num-i), i*dfs(num-i))
            dp[num] = max_prod
            return dp[num]
        return dfs(n)
            