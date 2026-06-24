class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(node, word):
            if not word:
                return node.word
            
            char, rest = word[0], word[1:]
            if char == ".":
                for child in node.children.values():
                    if dfs(child, rest):
                        return True
                return False
            elif char not in node.children:
                return False
            return dfs(node.children[char], rest)
            
        return dfs(self.root, word)