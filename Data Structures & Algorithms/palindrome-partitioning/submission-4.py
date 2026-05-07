class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(ind, curr):
            if ind == len(s):
                res.append(curr.copy())
                return
            for i in range(ind, len(s)):
                new_str = s[ind:i+1]
                if new_str == new_str[::-1]:
                    curr.append(new_str)
                    backtrack(i+1, curr)
                    curr.pop()
        backtrack(0, [])
        return res
