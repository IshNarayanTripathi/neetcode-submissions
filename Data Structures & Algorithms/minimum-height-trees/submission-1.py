class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[v].append(u)
            adj_list[u].append(v)

        def dfs(node, visited, level, curr):
            visited.add(node)
            for nei in adj_list[node]:
                if nei in visited:
                    curr.append(level)
                    continue
                visited.add(nei)
                dfs(nei, visited, level + 1, curr)

            return max(curr)

        min_height = float("inf")
        res = []
        for i in range(n):
            curr_height = dfs(i, set(), 0, [])
            if curr_height < min_height:
                res = [i]
                min_height = curr_height
            elif curr_height == min_height:
                res.append(i)

        return res