class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        n = len(nums)
        while True:
            fast += 2
            slow += 1
            if nums[fast%n] == nums[slow%n]:
                return nums[fast%n]
                
        
