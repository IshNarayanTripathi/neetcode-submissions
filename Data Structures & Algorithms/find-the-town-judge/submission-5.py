class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = defaultdict(list)
        
        for a,b in trust:
            trusted[a].append(b)
        res = -1
        for i in range(1, n+1):
            if i not in trusted:
                res = i
        if res != -1:
            for key in trusted.keys():
                if res not in trusted[key]:
                    return -1
        return res