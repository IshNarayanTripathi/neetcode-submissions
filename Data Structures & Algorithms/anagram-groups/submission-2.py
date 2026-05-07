class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            anagram[key].append(word)
        return [l for l in anagram.values()]