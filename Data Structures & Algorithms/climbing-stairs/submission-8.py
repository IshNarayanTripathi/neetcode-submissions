class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0]*(n+1)
        steps[1] = 1
        if 2 < n+1: steps[2] = 2
        for step in range(3, n+1):
            steps[step] = steps[step-1]+steps[step-2]
        return steps[n]