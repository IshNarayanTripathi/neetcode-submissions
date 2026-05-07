class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        strs.sort()
        length = min(len(strs[0]), len(strs[-1]))
        i = 0
        while i < length:
            if strs[0][i] != strs[-1][i]:
                break
            else:
                res += strs[0][i]
            i+=1
        return res
        