class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
    
        tl = [(t[0], t[1], i) for i, t in enumerate(tasks)]
        tl.sort(key = lambda x: (x[0], x[1]))
        tl = deque(tl)
        #heapq.heapify(tl)
        min_heap = []
        res = []
        timer = 0
        while tl or min_heap:
            while tl and tl[0][0] <= timer:
                enqueue, processing, index = tl.popleft()
                heapq.heappush(min_heap, (processing, enqueue, index))
            if min_heap:
                processing, enqueue, index = heapq.heappop(min_heap)
                timer += processing
                res.append(index)
            else:
                timer = tl[0][0]
        return res
                


