class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor_sum = 0
        def backtrack(ind, curr):
            nonlocal xor_sum
            if ind == len(nums):
                xor_sum += curr
                return
            
            backtrack(ind+1, curr^nums[ind])
          
            backtrack(ind+1, curr)
        backtrack(0, 0)
        return xor_sum
