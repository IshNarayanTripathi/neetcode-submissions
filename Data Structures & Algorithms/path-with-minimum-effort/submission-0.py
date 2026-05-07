class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        distance = [[float("inf")]*cols for i in range(rows)]
        distance[0][0] = 0
        min_heap = [(0, 0 ,0)]
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while min_heap:
            effort, r, c = heapq.heappop(min_heap) 
            if effort > distance[r][c]:
                continue
            if r == rows-1 and c == cols-1:
                return effort
            for x, y in directions:
                nr, nc = r+x, c+y
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_effort = max(effort, abs(heights[nr][nc]-heights[r][c]))
                    if distance[nr][nc] > new_effort:
                        distance[nr][nc] = new_effort
                        heapq.heappush(min_heap, (new_effort, nr, nc))
        return 0
        