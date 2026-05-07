class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def backtrack(ind, total):
            if ind >= len(cost):
                return total
            res = min(backtrack(ind+1, cost[ind]+total), backtrack(ind+2, cost[ind]+total))
            return res
        return min(backtrack(0, 0), backtrack(1, 0))
            