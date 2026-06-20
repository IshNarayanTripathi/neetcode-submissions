class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def maxBooty(ind):
            if ind >= len(nums):
                return 0
            if ind in dp:
                return dp[ind]
            cost = max(nums[ind]+maxBooty(ind+2), maxBooty(ind+1))
            dp[ind] = cost
            return dp[ind]
        return maxBooty(0)