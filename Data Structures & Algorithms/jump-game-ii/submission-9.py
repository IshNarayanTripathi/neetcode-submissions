class Solution:
    def jump(self, nums: list[int]) -> int:
        end = max_pos = jump = 0
        for i in range(len(nums)-1):
            max_pos = max(max_pos, i+nums[i])
            if i == end:
                jump += 1
                end = max_pos
        return jump