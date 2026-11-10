class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid = l+(r-l)//2
            if mid-1 >= 0 and mid+1 <= n-1 and nums[mid-1] >= nums[mid] <= nums[mid+1]:
                return nums[mid]
            if mid == n-1 and nums[mid] <= nums[mid-1]:
                return nums[mid]
            elif nums[l] <= nums[mid]:
                if nums[mid] >= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            elif nums[mid] <= nums[r]:
                if nums[mid] <= nums[l]:
                    r = mid-1
                else:
                    l = mid+1

