class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        res = []
        def backtrack(ind, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return
            for i in range(ind, n):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()
        backtrack(0, [])
        return res