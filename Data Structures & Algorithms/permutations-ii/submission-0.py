class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        pick = [False]*len(nums)
        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if pick[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not pick[i-1]:
                    continue
                
                pick[i] = True
                curr.append(nums[i])
                backtrack(curr)
                curr.pop()
                pick[i] = False
        backtrack([])
        return res