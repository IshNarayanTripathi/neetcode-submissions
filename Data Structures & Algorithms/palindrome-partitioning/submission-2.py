class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(start, curr):
            if start == len(s):
                res.append(curr.copy())
                return
            for end in range(start, len(s)):
                sub_str = s[start:end+1]
                if sub_str == sub_str[::-1]:
                    curr.append(sub_str)
                    backtrack(end+1, curr)
                    curr.pop()
        backtrack(0, [])
        return res