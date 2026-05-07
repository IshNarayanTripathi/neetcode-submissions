class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.priority = []

        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        heapq.heappush(self.priority, val)
        while len(self.priority) > self.size:
            heapq.heappop(self.priority)
        return self.priority[0]
