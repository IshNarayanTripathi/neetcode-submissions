class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        side = total // 4
        matchsticks.sort(reverse=True)
        sides = [0]*4
        def backtrack(ind):
            if ind == len(matchsticks):
                return all(s == side for s in sides)
            for i in range(4):
                if sides[i]+matchsticks[ind]<=side:
                    sides[i]+=matchsticks[ind]
                    if backtrack(ind+1):
                        return True
                    sides[i]-=matchsticks[ind]
            return False
        return backtrack(0)