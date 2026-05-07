class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda x:x[0])
        i, time = 0, tasks[0][0]
        res, min_heap = [], []
        while i < len(tasks) or min_heap:
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][2]))
                i+=1
            if not min_heap:
                time = tasks[i][0]
            else:
                procT, index = heapq.heappop(min_heap)
                time += procT
                res.append(index)
        return res