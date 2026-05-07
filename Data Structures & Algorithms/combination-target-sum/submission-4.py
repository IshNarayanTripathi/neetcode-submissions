class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        def backtrack(ind, curr, summ):
            if summ == target:
                res.append(curr.copy())
                return
            if ind == len(nums) or summ > target:
                return
            curr.append(nums[ind])
            backtrack(ind, curr, summ+nums[ind])
            curr.pop()
            backtrack(ind+1, curr, summ)
        backtrack(0, [], 0)
        return res