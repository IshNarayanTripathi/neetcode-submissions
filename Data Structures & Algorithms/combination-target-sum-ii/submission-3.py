class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        visited = set()
        res = []
        def backtrack(ind, curr, summ):
            if summ == target:
                if tuple(curr) not in visited:
                    res.append(curr.copy())
                    visited.add(tuple(curr.copy()))
                    return
            if summ > target or ind == len(candidates):
                return
            curr.append(candidates[ind])
            backtrack(ind+1, curr, summ+candidates[ind])
            curr.pop()
            backtrack(ind+1, curr, summ)
        backtrack(0, [], 0)
        return res