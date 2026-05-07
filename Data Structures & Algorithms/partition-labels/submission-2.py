class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        res = []
        curr_str = ""
        curr_set = set()
        i = 0
        while i < len(s):
            curr_str += s[i]
            count[s[i]] -= 1
            curr_set.add(s[i])
            if all(count[i] == 0 for i in curr_set):
                res.append(len(curr_str))
                curr_str = ""
                curr_set = set()
            i += 1
        return res