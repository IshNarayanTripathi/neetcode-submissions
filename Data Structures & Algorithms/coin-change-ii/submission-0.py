class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, remain):
            if remain == 0:
                return 1
            if remain < 0 or i >= len(coins):
                return 0
            if (i, remain) in dp:
                return dp[(i, remain)]
            dp[(i, remain)] = dfs(i, remain-coins[i])+dfs(i+1, remain)
            return dp[(i,remain)]
        return dfs(0, amount)