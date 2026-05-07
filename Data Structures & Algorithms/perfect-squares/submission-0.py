class Solution:
    def numSquares(self, n: int) -> int:
        sq = []
        for i in range(1, n+1):
            if self.isSquare(i):
                sq.append(i)
        dp = {}
        def dfs(curr):
            if curr == n:
                return 0
            if curr > n:
                return float("inf")
            if curr in dp:
                return dp[curr]
            min_ways = float("inf")
            for num in sq:
                min_ways = min(min_ways, 1+dfs(curr+num))
            dp[curr] = min_ways
            return dp[curr]
        return dfs(0)


    def isSquare(self, n):
        root = math.isqrt(n)
        return root*root == n