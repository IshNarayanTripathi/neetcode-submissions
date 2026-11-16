class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ts = sum(nums)
        p = (ts+target)/2
        pi = (ts+target)//2
        if p > pi:
            return 0
        if abs(target) > ts:
            return 0
        dp = [0]*(pi+1)
        dp[0] = 1
        for num in nums:
            for i in range(pi, num-1, -1):
                dp[i] += dp[i-num]
        return dp[pi]