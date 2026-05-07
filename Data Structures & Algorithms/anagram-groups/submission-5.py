class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort()
        res = defaultdict(list)
        for i in strs:
            key = ''.join(sorted(i))
            res[key].append(i)
        return [val for key, val in res.items()]
        