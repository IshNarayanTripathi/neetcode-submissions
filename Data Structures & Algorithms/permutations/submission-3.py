class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        taken = [False]*(len(nums))
        res = []
        def backtrack(ind, curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if not taken[i]:
                    taken[i] = True
                    curr.append(nums[i])
                    backtrack(i+1, curr)
                    curr.pop()
                    taken[i] = False
                    
        backtrack(0, [])
        return res