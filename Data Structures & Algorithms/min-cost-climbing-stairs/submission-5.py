class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def minCost(ind):
            if ind > len(cost)-1:
                return 0
            if ind == len(cost)-1:
                return cost[-1]
            if ind in dp:
                return dp[ind]
            total_cost = min(cost[ind]+minCost(ind+1), cost[ind]+ minCost(ind+2))
            dp[ind] = total_cost
            return dp[ind]
        return min(minCost(0), minCost(1))