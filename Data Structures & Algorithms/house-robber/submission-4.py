class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = max(dfs(i+2)+nums[i], dfs(i+1))
            return dp[i]
        return dfs(0)
    