class TimeMap:

    def __init__(self):
        self.tm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tm[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        res = self.tm[key]
        if not res:
            return ""
        l, r = 0, len(res)-1
        prev_val = ""
        while l <= r:
            mid = l + (r-l)//2
            if res[mid][0] == timestamp:
                return res[mid][1]
            elif res[mid][0] > timestamp:
                r = mid-1
            else:
                prev_val = res[mid][1]
                l = mid+1
        # for ts, val in res:
        #     if ts == timestamp:
        #         return val
        #     elif ts > timestamp:
        #         return prev_val
        #     else:
        #         prev_val = val
        return prev_val