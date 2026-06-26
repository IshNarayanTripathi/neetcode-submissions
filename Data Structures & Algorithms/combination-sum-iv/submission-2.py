class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(curr):
            if curr == target:
                return 1
            if curr > target:
                return 0
            
            if curr in dp:
                return dp[curr]
            res = 0
            for num in nums:
                res += dfs(curr+num)
            dp[curr] = res
            return dp[curr]
        return dfs(0)