class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [(-freq,char) for char,freq in count.items()]
        heapq.heapify(max_heap)
        time = 0
        tracker = deque()
        while max_heap or tracker:
            if tracker and tracker[0][0] == time:
                heapq.heappush(max_heap, (tracker.popleft()[1:]))
            if max_heap:
                freq,char= heapq.heappop(max_heap)
                freq +=1
                if freq < 0:
                    tracker.append((time+n+1,freq,char))
            
            time += 1
        return time

