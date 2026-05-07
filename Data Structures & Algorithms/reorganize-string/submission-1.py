class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [(-freq, key) for key, freq in count.items()]
        heapq.heapify(max_heap)
        curr = ""
        prev_char = None
        prev_val = float("inf")
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            if prev_char:
                if prev_char == char:
                    return ""
            curr += char
            if prev_val < 0:
                heapq.heappush(max_heap, (prev_val, prev_char))
            prev_char = char
            prev_val = freq+1
        return curr if len(curr) == len(s) else ""

            
