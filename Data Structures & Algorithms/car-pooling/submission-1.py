class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_heap = [(fro, to, pas) for pas,fro,to in trips]
        heapq.heapify(max_heap)
        curr_capacity = 0
        prev_stop = 0
        prev_pas = 0
        while max_heap:
            fro, to, pas = heapq.heappop(max_heap)
            if prev_stop:
                if fro < prev_stop:
                    curr_capacity += pas
                    if curr_capacity > capacity:
                        return False
                else:
                    curr_capacity -= prev_pas
                    curr_capacity += pas
                prev_stop = to
                prev_pas = pas
            else:
                curr_capacity +=  pas
                prev_stop = to
                prev_pas = pas
        return True


