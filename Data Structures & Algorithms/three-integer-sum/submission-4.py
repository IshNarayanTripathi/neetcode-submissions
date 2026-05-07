class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        added = set()
        nums.sort()
        for i, val in enumerate(nums):
            left = i+1
            right = len(nums)-1
            while left < right:
                if val + nums[left] + nums[right] == 0:
                    if tuple((val, nums[left], nums[right])) not in added:
                        res.append([val, nums[left], nums[right]])
                        added.add(tuple((val, nums[left], nums[right])))
                    left += 1
                    right -= 1
                elif val + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return res