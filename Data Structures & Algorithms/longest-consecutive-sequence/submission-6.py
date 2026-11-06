class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        prev = nums[0]
        max_val = curr = 1
        for i in nums[1:]:
            if i == prev:
                continue
            elif i == prev+1:
                prev = i
                curr += 1
                max_val = max(max_val, curr)
            else:
                prev = i
                max_val = max(max_val, curr)
                curr = 1
        return max_val            