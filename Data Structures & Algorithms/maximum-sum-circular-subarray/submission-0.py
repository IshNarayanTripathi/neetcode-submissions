class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def maximum(x):
            max_sum = curr_sum = x[0]
            for num in x[1:]:
                curr_sum = max(curr_sum+num, num)
                max_sum = max(max_sum, curr_sum)
            return max_sum
        def minimum(x):
            min_sum = curr_sum = x[0]
            for num in x[1:]:
                curr_sum = min(curr_sum+num, num)
                min_sum = min(min_sum, curr_sum)
            return min_sum
        maxi = maximum(nums)
        mini = minimum(nums)
        total = sum(nums)
        if maxi < 0:
            return maxi
        return max(maxi, total-mini)