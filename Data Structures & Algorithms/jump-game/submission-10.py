class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos = nums[0]
        curr_pos = nums[0]
        last_index = len(nums)-1
        i = 1 if len(nums) > 1 else 0
        while i <= max_pos:
            curr_pos = i+nums[i]
            i += 1
            max_pos = max(max_pos, curr_pos)
            if max_pos >= last_index:
                return True
        return False