class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(ind, curr):
            if ind == len(s):
                res.append(curr.copy())
                return
            for i in range(ind, len(s)):
                sub_str = s[ind:i+1]
                if sub_str == sub_str[::-1]:
                    curr.append(sub_str)
                    backtrack(i+1, curr)
                    curr.pop()
        backtrack(0, [])
        return res