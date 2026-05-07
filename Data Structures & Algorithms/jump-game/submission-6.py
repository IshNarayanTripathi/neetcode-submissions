class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for i in range(len(nums)):
            if i > reachable:
                return False
            
            #reachable += nums[i]
            reachable = max(i+nums[i], reachable)
            
        return True