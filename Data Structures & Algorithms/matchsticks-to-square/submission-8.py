class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total%4 != 0:
            return False
        matchsticks.sort(reverse=True)
        square = [0]*4
        target = total // 4
        def backtrack(ind):
            if ind == len(matchsticks):
                return all(b == target for b in square)
            for i in range(4):
                if square[i] + matchsticks[ind] <= target:
                    square[i] += matchsticks[ind]
                    if backtrack(ind+1):
                        return True
                    square[i] -= matchsticks[ind]

                if not square[i]:
                    break
            return False

        return backtrack(0)