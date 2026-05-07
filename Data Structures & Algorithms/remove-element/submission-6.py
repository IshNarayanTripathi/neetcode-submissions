class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[j] = nums[i]
                j += 1
        return j