class Solution:
    def minCostClimbingStairs(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = nums[i] +  min(dfs(i+1), dfs(i+2))
            return dp[i]
        min_cost = min(dfs(0),dfs(1))
        return min_cost
        