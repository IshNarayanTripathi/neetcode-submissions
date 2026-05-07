class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
        min_jump = float("inf")
        def dfs(i, count):
            nonlocal min_jump
            if i == len(nums)-1:
                min_jump = min(min_jump, count)
                return
            if i >= len(nums):
                return float("inf")
            for jump in range(1, nums[i]+1):
                dfs(i+jump, count+1)
        dfs(0,0)
        return min_jump
            