class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_by = defaultdict(list)
        for a, b in trust:
            trusted_by[b].append(a)
        for i in range(1, n+1):
            if len(trusted_by[i]) == n-1:
                correct = True
                for values in trusted_by[i]:
                    if i in trusted_by[values]:
                        correct = False
                if correct:
                    return i
        return -1