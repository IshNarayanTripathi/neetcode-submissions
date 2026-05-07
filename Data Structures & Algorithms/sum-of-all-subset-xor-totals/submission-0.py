class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor_sum = 0
        def backtrack(ind, curr):
            nonlocal xor_sum
            if ind == len(nums):
                curr_sum = 0
                for num in curr:
                    curr_sum ^= num
                xor_sum += curr_sum
                return
            curr.append(nums[ind])
            backtrack(ind+1, curr)
            curr.pop()
            backtrack(ind+1, curr)
        backtrack(0, [])
        return xor_sum
