class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def backtrack(ind):
            if ind >= len(nums):
                return 0
            if ind in dp:
                return dp[ind]
            dp[ind] = max(nums[ind]+backtrack(ind+2), backtrack(ind+1))
            return dp[ind]
        return backtrack(0)