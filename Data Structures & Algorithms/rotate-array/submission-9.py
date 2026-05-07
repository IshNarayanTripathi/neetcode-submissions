class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n != 1 and n != k:
            k = k % n
            nums[:] = nums[n-k:]+nums[:n-k]