class Node:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.eow = True

    def search(self, word: str) -> bool:

        def dfs(root, start):
            curr = root
            for i in range(start, len(word)):
                char = word[i]
                if char == ".":
                    for child in curr.children.values():
                        if dfs(child, i+1):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.eow
        return dfs(self.root, 0)





