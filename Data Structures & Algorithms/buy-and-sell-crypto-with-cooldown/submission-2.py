class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            res = dfs(i+1, buying)
            if buying:
                res = max(res, -prices[i]+dfs(i+1, not buying))
            else:
                res = max(res, +prices[i]+dfs(i+2, not buying))
            dp[(i, buying)] = res
            return dp[(i, buying)]
        return dfs(0, True)