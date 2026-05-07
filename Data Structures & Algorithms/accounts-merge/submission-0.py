class DFS:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x] 

    def union(self, u, v):
        parent_v, parent_u = self.find(v), self.find(u)
        if parent_v == parent_u:
            return False
        self.parent[parent_v] = parent_u
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = DFS(len(accounts))
        emailToName = {}
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToName:
                    uf.union(i, emailToName[e])
                else:
                    emailToName[e] = i
        emailGroup = defaultdict(list)
        for e, i in emailToName.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)
        res = []
        for i, e in emailGroup.items():
            res.append([accounts[i][0]]+sorted(e))
        return res



        