class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        matchsticks.sort(reverse=True)
        target = total // 4
        block = [0]*4
        def backtrack(ind):
            if ind == len(matchsticks):
                return all(b == target for b in block)
            for i in range(4):
                if block[i] + matchsticks[ind] <= target:
                    block[i] += matchsticks[ind]
                    if backtrack(ind+1):
                        return True
                    block[i] -= matchsticks[ind]
                if block[i] == 0:
                    break
            return False
        return backtrack(0)