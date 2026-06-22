class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(curr, ind):
            if curr == 0:
                return 0
            if curr < 0 or ind >= len(coins):
                return float("inf")
            if (curr, ind) in dp:
                return dp[(curr, ind)]
            take = 1+dfs(curr-coins[ind], ind)
            skip = dfs(curr, ind+1)
            dp[(curr, ind)] = min(take, skip)
            return dp[(curr, ind)]
        res = dfs(amount, 0)
        return res if res != float("inf") else -1