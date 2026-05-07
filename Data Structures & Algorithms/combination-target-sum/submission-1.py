class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(ind, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or ind == len(nums):
                return
            curr.append(nums[ind])
            backtrack(ind,curr,total+nums[ind])
            curr.pop()
            backtrack(ind+1,curr,total)
        backtrack(0,[],0)
        return res