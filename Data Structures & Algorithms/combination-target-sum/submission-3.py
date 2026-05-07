class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        visited = set()
        def backtrack(ind, curr, summ):
            if summ == target:
                if tuple(curr) not in visited:
                    res.append(curr.copy())
                    visited.add(tuple(curr.copy()))
            if ind == len(nums) or summ > target:
                return
            curr.append(nums[ind])
            backtrack(ind, curr, summ+nums[ind])
            curr.pop()
            backtrack(ind+1, curr, summ)
        backtrack(0, [], 0)
        return res