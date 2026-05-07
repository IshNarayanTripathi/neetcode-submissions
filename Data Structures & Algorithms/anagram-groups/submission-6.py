class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for val in strs:
            key = ''.join(sorted(val))
            res[key].append(val)
        return [val for val in res.values()]