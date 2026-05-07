class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for i in strs:
            key = ''.join(sorted(i))
            group[key].append(i)
        return [i for i in group.values()]