class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = [i for i in range(1, n+1)]
        def backtrack(ind, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return
            if ind == n:
                return
            curr.append(nums[ind])
            backtrack(ind+1, curr)
            curr.pop()
            backtrack(ind+1, curr)
        backtrack(0, [])
        return res