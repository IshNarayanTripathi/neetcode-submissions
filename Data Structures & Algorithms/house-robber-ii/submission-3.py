class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def smart_choice(arr):
            dp = {}
            def backtrack(ind):
                if ind >= len(arr):
                    return 0
                if ind in dp:
                    return dp[ind]
                dp[ind] = max(arr[ind]+backtrack(ind+2), backtrack(ind+1))
                return dp[ind]
            return backtrack(0)
        return max(smart_choice(nums[:-1]), smart_choice(nums[1:]))
