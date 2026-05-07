class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(list)
        variables = set()
        for i in range(len(values)):
            u, v = equations[i][0], equations[i][1]
            adj_list[u].append((v, values[i]))
            adj_list[v].append((u, 1/values[i]))
            variables.add(u)
            variables.add(v)
        def dfs(start, target, effort, visited):
            if start == target:
                return effort
            visited.add(start)
            for nei, e in adj_list[start]:
                if nei not in visited:
                    res = dfs(nei, target, effort*e, visited)
                    if res != -1.0:
                        return res
            return -1.0
        res = []
        for u, v in queries:
            if u not in variables or v not in variables:
                res.append(-1.0)
                continue
            res.append(dfs(u, v, 1.0, set()))
        return res

            
