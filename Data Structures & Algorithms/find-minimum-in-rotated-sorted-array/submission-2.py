class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        min_val = float("inf")
        while left <= right:
            mid = left+(right-left)//2
            min_val = min(min_val, nums[mid])
            if nums[mid] > nums[right]:
                left = mid+1
            elif nums[mid] > nums[left] or nums[left] > nums[right]:
                right = mid-1
           
            else:
                return min_val 
        
