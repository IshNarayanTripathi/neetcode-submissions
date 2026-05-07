class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(ind, curr):
            res.append(curr.copy())
            for i in range(ind, len(nums)):
                if i > ind and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()
        backtrack(0, [])
        return res