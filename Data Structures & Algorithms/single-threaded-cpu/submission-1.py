class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for  i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda x: x[0])
        result = []
        i, time = 0, tasks[0][0]
        min_heap = []
        while i < len(tasks)  or min_heap:
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][2]))
                i+=1
            if not min_heap:
                time = tasks[i][0]
            if min_heap:
                Proct, index = heapq.heappop(min_heap)
                result.append(index)
                time +=  Proct
        return result