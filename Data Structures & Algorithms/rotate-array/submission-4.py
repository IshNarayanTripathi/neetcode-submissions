class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return
        k %= n
        nums[:] = nums[n - k:] + nums[:n - k]
