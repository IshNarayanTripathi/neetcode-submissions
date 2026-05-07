class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        taken = [False]*len(nums)
        res = []
        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if taken[i]:
                    continue
                taken[i] = True
                curr.append(nums[i])
                backtrack(curr)
                curr.pop()
                taken[i] = False
        backtrack([])
        return res