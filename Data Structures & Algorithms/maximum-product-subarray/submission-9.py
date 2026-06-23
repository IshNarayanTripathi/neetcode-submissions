class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = curr_max = curr_min = nums[0]
        for num in nums[1:]:
            temp = curr_max
            curr_max = max(curr_max*num, num, curr_min*num)
            curr_min = min(temp*num, num, curr_min*num)
            global_max = max(global_max, curr_max)
        return global_max