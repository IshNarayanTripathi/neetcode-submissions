class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        added = set()
        for i, val in enumerate(nums):
            for j in range(i+1, len(nums)):
                val2 = nums[j]
                left = j + 1
                right = len(nums)-1
                while left < right:
                    total = val + val2 + nums[left] + nums[right]
                    if total == target:
                        if tuple((val, val2, nums[left], nums[right])) not in added:
                            res.append([val, val2, nums[left], nums[right]])
                            added.add(tuple((val, val2, nums[left], nums[right])))
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total > target:
                        right -= 1
                    else:
                        left += 1
        return res