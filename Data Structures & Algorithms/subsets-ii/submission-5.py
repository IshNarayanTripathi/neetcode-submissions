class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        visited = set()
        def backtrack(ind, curr):
            if ind == len(nums):
                if tuple(curr) not in visited:
                    visited.add(tuple(curr.copy()))
                    res.append(curr.copy())
                return
            curr.append(nums[ind])
            backtrack(ind+1, curr)
            curr.pop()
            backtrack(ind+1, curr)
        backtrack(0, [])
        return res