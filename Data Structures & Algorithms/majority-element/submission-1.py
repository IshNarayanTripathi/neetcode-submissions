class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_val = nums[0]
        cnt = 0
        for i in range(len(nums)):
            cnt = cnt+1 if nums[i] == max_val else cnt-1
            if cnt <= 0:
                max_val = nums[i]
        return max_val
