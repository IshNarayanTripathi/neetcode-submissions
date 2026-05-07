class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(ind, curr_sum, curr_list):
            if ind == len(nums) or curr_sum > target:
                return
            if curr_sum == target:
                res.append(curr_list.copy())
                return
            curr_list.append(nums[ind])
            backtrack(ind, curr_sum+nums[ind], curr_list)
            curr_list.pop()
            
            backtrack(ind+1, curr_sum, curr_list)

        backtrack(0, 0, [])
        return res