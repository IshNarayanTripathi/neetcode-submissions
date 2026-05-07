class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-freq for freq in count.values()]
        time = 0
        tracker = deque()
        while max_heap or tracker:
            time += 1
            if max_heap:
                freq = 1+heapq.heappop(max_heap)
                if freq:
                    tracker.append((freq, time+n))
            if tracker and tracker[0][1] == time:
                heapq.heappush(max_heap, tracker.popleft()[0])
        return time