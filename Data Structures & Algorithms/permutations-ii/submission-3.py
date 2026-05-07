class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        taken = [False]*len(nums)
        res = []
        visited = set()
        def backtrack(curr):
            if len(curr) == len(nums):
                if tuple(curr) not in visited:
                    visited.add(tuple(curr.copy()))
                    res.append(curr.copy())
                return
            for i in range(len(nums)):
                if not taken[i]:
                    taken[i] = True
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop()
                    taken[i] = False
        backtrack([])
        return res