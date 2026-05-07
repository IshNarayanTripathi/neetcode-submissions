class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = set()
        res = []
        def backtrack(ind, curr):
            if ind == len(nums):
                if tuple(curr) not in visited:
                    res.append(curr.copy())
                    visited.add(tuple(curr.copy()))
                return
            curr.append(nums[ind])
            backtrack(ind+1, curr)
            curr.pop()
            backtrack(ind+1, curr)
        backtrack(0, [])
        return res