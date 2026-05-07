class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            curr = nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[left]+nums[right]+curr == 0:
                    res.add((curr, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left]+nums[right]+curr > 0:
                    right -= 1
                else:
                    left += 1
        return list(res)