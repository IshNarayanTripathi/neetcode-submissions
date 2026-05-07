class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        max_len = min(len(strs[0]), len(strs[-1]))
        i = 0
        isValid = True
        while i < max_len and isValid:
            if strs[0][i] != strs[-1][i]:
                isValid = False
            else:
                i += 1
        return strs[0][:i]
            
