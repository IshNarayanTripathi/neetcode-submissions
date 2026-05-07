class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        pick = [False]*len(nums)
        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    pick[i] = True
                    curr.append(nums[i])
                    backtrack(curr)
                    pick[i] = False
                    curr.pop()
        backtrack([])
        return res