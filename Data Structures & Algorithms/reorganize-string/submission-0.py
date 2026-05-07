class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [(-freq, key) for key, freq in count.items()]
        heapq.heapify(max_heap)
        result = ""
        prev_key, prev_freq = None, 0
        while max_heap:
            freq, key = heapq.heappop(max_heap)
            result += key
            freq += 1
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_key))
            if freq < 0:
                prev_key = key
                prev_freq = freq
            else:
                prev_key = None
                prev_freq = 0
            
        return result if len(result) == len(s) else ""