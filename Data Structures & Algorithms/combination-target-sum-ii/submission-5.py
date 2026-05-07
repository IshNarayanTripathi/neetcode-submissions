class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        visited = set()
        def backtrack(ind, curr, curr_sum):
            if curr_sum == target:
                if tuple(curr) not in visited:
                    res.append(curr.copy())
                    visited.add(tuple(curr.copy()))
                return
            if ind >= len(nums) or curr_sum > target:
                return
            curr.append(nums[ind])
            backtrack(ind+1, curr, curr_sum+nums[ind])
            curr.pop()
            backtrack(ind+1, curr, curr_sum)
        backtrack(0, [], 0)
        return res