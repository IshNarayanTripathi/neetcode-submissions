class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        res = -1
        l = defaultdict(list)
        for a, b in trust:
            l[a].append(b)
        for i in range(1, n+1):
            if i not in l:
                res = i
        if res != -1:
            for key in l.keys():
                if res not in l[key]:
                    return -1
        return res