class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def dfs(l, r):
            if l == r:
                return piles[l]
            if (l, r) in dp:
                return dp[(l, r)]
            take_left = piles[l] - dfs(l+1, r)
            take_right = piles[r] - dfs(l, r-1)
            dp[(l, r)] = max(take_left, take_right)
            return dp[(l, r)]
        return dfs(0, len(piles)-1)>0
        

            
            
            