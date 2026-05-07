class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        if not tasks:
            return []
        res = []
        tasks = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        tasks = deque(sorted(tasks, key = lambda x: (x[0])))
        min_heap = []
        timer = 0
        while tasks or min_heap:
            while tasks and tasks[0][0]  <= timer:
                enqueue, process, ind = tasks.popleft()
                heapq.heappush(min_heap, (process, ind, enqueue))
            if min_heap:
                process, ind, _ = heapq.heappop(min_heap)
                timer += process
                res.append(ind)
            else:
                timer = tasks[0][0]
        return res