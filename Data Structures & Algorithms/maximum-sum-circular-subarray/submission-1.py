class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def maximum(nums):
            max_sum = curr_sum = nums[0]
            for num in nums[1:]:
                curr_sum = max(num, curr_sum+num)
                max_sum = max(curr_sum, max_sum)
            return max_sum
        def minimum(nums):
            min_sum = curr_sum = nums[0]
            for num in nums[1:]:
                curr_sum = min(num, curr_sum+num)
                min_sum =min(min_sum, curr_sum)
            return min_sum
        maxi = maximum(nums)
        mini = minimum(nums)
        if maxi < 0:
            return maxi
        return max(maxi, sum(nums)-mini)

