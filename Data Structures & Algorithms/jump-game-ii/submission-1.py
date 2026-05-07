class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp = {}
        
        def dfs(i):
        
            if i >= len(nums)-1:
                return 0
            if i in dp:
                return dp[i]
            min_jump = float("inf")
            for jump in range(1, nums[i]+1):
                min_jump = min(min_jump, 1+dfs(i+jump))
            dp[i] = min_jump
            return dp[i]
        return dfs(0)
        
            