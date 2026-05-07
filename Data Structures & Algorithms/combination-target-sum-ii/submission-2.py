class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(ind, curr_sum, curr_list):
            if curr_sum > target:
                return
            if curr_sum == target:
                res.append(curr_list.copy())
                return
            prev = -1
            for i in range(ind, len(candidates)):
                if candidates[i] == prev:
                    continue
                if curr_sum + candidates[i] > target:
                    break
                curr_list.append(candidates[i])
                backtrack(i+1, curr_sum+candidates[i], curr_list)
                curr_list.pop()
                prev = candidates[i]
        backtrack(0, 0, [])
        return res
