class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = set()
        res = []
        taken = [False]*len(nums)
        def backtrack(ind, curr):
            if len(curr) == len(nums):
                if tuple(curr) not in visited:

                    res.append(curr.copy())
                    visited.add(tuple(curr.copy()))
                    return
            for i in range(len(nums)):
                if not taken[i]:
                    taken[i] = True
                    curr.append(nums[i])
                    backtrack(i+1, curr)
                    taken[i] = False
                    curr.pop()
        backtrack(0, [])
        return res




