class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        str1 = [''.join(sorted(i)) for i in strs]
        str2 = set(str1)
        for key in str1:
            curr = []
            for i in range(len(strs)):
                if key == str1[i]:
                    curr.append(strs[i])
            if curr not in res:
                res.append(curr)
        return res
        