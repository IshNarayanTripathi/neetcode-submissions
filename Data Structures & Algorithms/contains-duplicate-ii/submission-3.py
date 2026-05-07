class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k >= len(nums):
            if len(set(nums)) != len(nums):
                return True
            return False
        
        left = 0
        for right in range(k, len(nums)):
            s = set(nums[left:right+1])
            if len(s) != right-left+1:
                return True
            left += 1
        return False
