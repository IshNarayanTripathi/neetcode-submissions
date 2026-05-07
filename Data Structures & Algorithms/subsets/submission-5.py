class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(ind, curr):
            if ind == len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[ind])
            backtrack(ind+1, curr)
            curr.pop()
            backtrack(ind+1, curr)
        backtrack(0, [])
        return res
            