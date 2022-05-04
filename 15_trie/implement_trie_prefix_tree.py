class TrieNode:
    def __init__(self, parent, cnt) -> None:
        self.children = {}  # dict ch-> new node
        self.is_word = False
        self.parent = parent
        self.cnt = cnt  # how many words end here


class Trie:  # reference sfxly-gk
    # https://leetcode.cn/problems/implement-trie-prefix-tree
    def __init__(self):
        self.root = TrieNode(None, 0)

    def insert(self, word: str) -> None:
        self.find(word, False, True)

    def search(self, word: str) -> bool:
        return self.find(word, True, False)

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix, False, False)

    def find(self, s: str, exact_match: bool, insert_if_not_exist: bool):
        curr = self.root
        for ch in s:
            if ch not in curr.children:
                if insert_if_not_exist:
                    curr.children[ch] = TrieNode(curr, 0)
                else:
                    return False
            curr = curr.children[ch]
        # add count at end ch of the word
        if insert_if_not_exist:
            curr.cnt += 1
        if not exact_match:
            return True
        return curr.cnt > 0  # exact match, return count


class Trie2:
    # https://leetcode.cn/problems/implement-trie-prefix-tree
    def __init__(self):
        # count: cnt of words end at current char, dict ch-> new node of structure [0, {}]
        self.root = [0, {}]

    def insert(self, word: str) -> None:
        self.find(word, False, True)

    def search(self, word: str) -> bool:
        return self.find(word, False, False)

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix, True, False)

    def find(self, s: str, prefix_match: bool, insert_if_not_exist: bool):
        curr = self.root
        for ch in s:
            if ch not in curr[1]:
                if insert_if_not_exist:
                    curr[1][ch] = [0, {}]
                else:
                    return False
            curr = curr[1][ch]
        # add count at end ch of the word
        if insert_if_not_exist:
            curr[0] += 1
        if prefix_match:
            return True
        return curr[0] > 0  # exact match, return count