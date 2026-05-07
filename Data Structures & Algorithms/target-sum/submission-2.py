class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, curr):
            if curr == target and i == len(nums):
                return 1
            if i >= len(nums):
                return 0
            if (i, curr) in dp:
                return dp[(i, curr)]
            plus = dfs(i+1, curr+nums[i])
            minus =  dfs(i+1, curr-nums[i])
            dp[(i, curr)] = plus+minus
            return dp[(i, curr)]
        return dfs(0, 0)
