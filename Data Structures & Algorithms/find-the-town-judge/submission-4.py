class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = defaultdict(set)
        trusting = [False]*(n+1)
        for a,b in trust:
            trusted[a].add(b)
            trusting[a] = True
        for i in range(1, n+1):
            all = True
            if not trusting[i]:
                for j in trusted:
                    if i not in trusted[j]:
                        all = False
                        break
                if all:
                    return i 
        return -1