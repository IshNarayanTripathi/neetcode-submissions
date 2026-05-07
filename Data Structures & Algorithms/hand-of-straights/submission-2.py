class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        count = Counter(hand)
        min_heap = [key for key in count.keys()]
        heapq.heapify(min_heap)
        while min_heap:
            first = min_heap[0]
            for i in range(groupSize):
                num = first+i
                if count[num] == 0:
                    return False
                count[num] -= 1
                if not count[num]:
                    if num == min_heap[0]:
                        heapq.heappop(min_heap)
                    else:
                        return False
              
            
        return True
                    