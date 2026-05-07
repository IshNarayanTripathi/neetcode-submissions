class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjaceny_list = {i:[] for i in range(n)}
        for s, des, w in edges:
            adjaceny_list[s].append([des, w])
        shortest = {}
        minheap = [[0, src]]
        while minheap:
            w1, n1 = minheap.pop(0)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            for n2, w2 in adjaceny_list[n1]:
                if n2 not in shortest:
                    minheap.append([w2+w1, n2])
            minheap.sort()
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest