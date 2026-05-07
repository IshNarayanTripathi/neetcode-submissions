class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                res.append(nums[i])
        for i in res:
            nums.remove(i)
        return len(nums)