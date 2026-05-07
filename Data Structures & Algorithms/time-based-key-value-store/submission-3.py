from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.time:
            left, right = 0, len(self.time[key])-1
            res = ""
            while left <= right:
                mid = left+(right-left)//2
                if self.time[key][mid][0] == timestamp:
                    return self.time[key][mid][1]
                elif self.time[key][mid][0] > timestamp:
                    right = mid-1
                else:
                    res = self.time[key][mid][1]
                    left = mid+1
            return res
        return ""
            