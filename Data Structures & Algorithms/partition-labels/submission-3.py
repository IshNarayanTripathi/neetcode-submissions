class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        n = len(s)
        l = 0
        res = []
        block = set()
        for r in range(n):
            block.add(s[r])
            count[s[r]] -= 1
            if all(count[b] == 0 for b in block):
                res.append(r-l+1)
                l = r+1
                block.clear()
        return res
