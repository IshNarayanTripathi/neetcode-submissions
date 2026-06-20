class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def pure(arr):
            dp = {}
            def maxBooty(ind):
                if ind >= len(arr):
                    return 0
                if ind in dp:
                    return dp[ind]
                cost = max(arr[ind]+maxBooty(ind+2), maxBooty(ind+1))
                dp[ind] = cost
                return dp[ind]
            return maxBooty(0)
        return max(pure(nums[:-1]), pure(nums[1:]))