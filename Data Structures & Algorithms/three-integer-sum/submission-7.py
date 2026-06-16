class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            curr = nums[i]
            left, right = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                if curr + nums[left] + nums[right] == 0:
                    res.append([curr, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while right > left and right+1 < len(nums) and nums[right] == nums[right+1]:
                        right -= 1
                    while right > left > 0 and nums[left] == nums[left-1]:
                        left += 1

                elif curr + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return res