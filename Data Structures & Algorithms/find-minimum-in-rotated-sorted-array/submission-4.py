class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                # min is in the right half
                left = mid + 1
            else:
                # min is in the left half (including mid)
                right = mid
        return nums[left]
            