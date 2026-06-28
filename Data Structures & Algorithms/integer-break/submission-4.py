class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        def dfs(curr, prod):
            if curr == n:
                return prod
            if curr > n:
                return float("-inf")
            if (curr, prod) in dp:
                return dp[(curr, prod)]
            res = float("-inf")
            for i in range(1, n):
                if curr+i>n:
                    break
                res = max(res, dfs(i+curr, prod*i))
            dp[(curr, prod)] = res
            return dp[(curr, prod)]
        return dfs(0, 1)
