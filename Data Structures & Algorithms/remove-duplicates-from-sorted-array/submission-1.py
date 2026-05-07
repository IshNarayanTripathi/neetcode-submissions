class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = [i for i in set(nums)]
        nums.sort()
        return len(nums)
