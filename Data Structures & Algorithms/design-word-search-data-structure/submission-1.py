class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(root, j):
            curr = root
            for i in range(j, len(word)):
                letter = word[i]
                if letter == ".":
                    for child in curr.children.values():
                        if dfs(child, i+1):
                            return True
                    return False
                else:
                    if letter not in curr.children:
                        return False
                    curr = curr.children[letter]
            return curr.end
        return dfs(self.root, 0)



