# https://leetcode.cn/problems/design-add-and-search-words-data-structure/?envType=study-plan-v2&envId=top-interview-150


class TrieNode:
    def __init__(self) -> None:
        self.cnt = 0  # how many nodes end here
        self.c2node_map: dict[str, TrieNode] = {}


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        self._find(word, insert_if_not_found=True)

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix)

    def search(self, word: str) -> bool:
        return self._find(word, exact_match=True)

    def _find(
        self, s: str, exact_match: bool = False, insert_if_not_found: bool = False
    ) -> bool:
        curr = self.root
        for c in s:
            if c not in curr.c2node_map:
                if insert_if_not_found:
                    curr.c2node_map[c] = TrieNode()
                else:
                    return False
            curr = curr.c2node_map[c]
        if insert_if_not_found:
            curr.cnt += 1
        if not exact_match:
            return True
        return curr.cnt > 0


class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word=word)

    def search(self, word: str) -> bool:
        def dfs(index: int, trie_node: TrieNode) -> bool:
            if index == len(word):
                return trie_node.cnt > 0
            c = word[index]
            if c != ".":  # this specific subproblem is true
                child = trie_node.c2node_map.get(c, None)
                if child and dfs(index + 1, child):
                    return True
            else:  # any subproblem is true, that means matched
                for child in trie_node.c2node_map.values():
                    if child and dfs(index + 1, child):
                        return True
            return False

        return dfs(
            index=0,
            trie_node=self.trie.root,
        )


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
