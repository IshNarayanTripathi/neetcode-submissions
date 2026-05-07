class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, curr):
            if curr == amount:
                return 1
            if curr > amount or i >= len(coins):
                return 0
            if (i, curr) in dp:
                return dp[(i, curr)]
            take = dfs(i, curr+coins[i])
            skip = dfs(i+1, curr)
            dp[(i, curr)] = skip+take
            return dp[(i, curr)]
        return dfs(0, 0)