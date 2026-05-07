class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        pick = [False]*len(nums)
        def backtrack(curr):
            if len(curr) == len(nums):
                if tuple(curr) not in visited:
                    res.append(curr.copy())
                    visited.add(tuple(curr.copy()))
                    return
            for i in range(len(nums)):
                if not pick[i]:
                    pick[i] = True
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop()
                    pick[i] = False
        backtrack([])
        return res