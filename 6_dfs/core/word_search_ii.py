import collections
from typing import List


class TrieNode:
    def __init__(self, parent, cnt) -> None:
        self.c2node_map: dict[str, TrieNode] = {}  # dict ch-> new node
        self.parent = parent
        self.cnt = cnt  # how many words end here


class Trie:
    # https://leetcode.cn/problems/implement-trie-prefix-tree
    def __init__(self):
        self.root = TrieNode(None, 0)

    def insert(self, word: str) -> None:
        self.find(word, False, True)

    def search(self, word: str) -> bool:
        return self.find(word, False, False)

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix, True, False)

    def find(self, s: str, prefix_match: bool, insert_if_not_exist: bool):
        curr = self.root
        for ch in s:
            if ch not in curr.c2node_map:
                if insert_if_not_exist:
                    curr.c2node_map[ch] = TrieNode(curr, 0)
                else:
                    return False
            curr = curr.c2node_map[ch]
        # add count at end ch of the word
        if insert_if_not_exist:
            curr.cnt += 1
        if prefix_match:
            return True
        return curr.cnt > 0  # exact match, return count


class Solution:
    # char矩阵中找1个单词  https://leetcode.cn/problems/word-search/
    def exist(self, board: List[List[str]], words: str) -> bool:
        return len(self.findWords(board, [words])) > 0

    def inside(self, board: List[List[str]], x: int, y: int):
        return 0 <= x < len(board) and 0 <= y < len(board[0])

    # char矩阵中找多个单词words 返回找到的无重复词集  https://leetcode.cn/problems/word-search-ii
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        results = []
        path = []
        visited = collections.defaultdict(bool)
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited[(i, j)] = True
                path.append(board[i][j])
                self.dfs(board, i, j, path, results, visited, trie.root)
                path.pop()
                visited[(i, j)] = False
        return results

    def dfs(
        self,
        board: List[List[str]],
        i: int,
        j: int,
        path: list[str],
        results: list[str],
        visited: dict[tuple[int, int], bool],
        node: TrieNode,
    ):
        c = board[i][j]
        if c not in node.c2node_map:  # non-existent route
            return
        curr = node.c2node_map[c]
        if curr.cnt > 0:
            results.append("".join(path))
            curr.cnt = 0  # prevent dups
        if not curr.c2node_map:
            del node.c2node_map[c]
            return
        # 剪枝优化 如果当前节点没孩子 从父节点删掉当前节点信息(kv) return
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx = i + dx
            ny = j + dy
            if visited[(nx, ny)]:
                continue
            if not self.inside(board, nx, ny):
                continue
            visited[(nx, ny)] = True
            path.append(board[nx][ny])
            self.dfs(board, nx, ny, path, results, visited, curr)
            path.pop()
            visited[(nx, ny)] = False


class Solution2:
    """word search ii 不用trie 以下是用prefix set的解法 lc judge会超时"""

    """https://www.lintcode.com/problem/132/?_from=collection&fromId=161
    Description
Given a matrix of lower alphabets and a dictionary. Find all words in the dictionary that can be found in the matrix.
A word can start from any position in the matrix and go left/right/up/down to the adjacent position.
One character only be used once in one word. No same word in dictionary

Example 1:

Input：board = ["doaf","agai","dcan"]，words = ["dog","dad","dgdg","can","again"]
Output：["again","can","dad","dog"]
Explanation：
  d o a f
  a g a i
  d c a n
search in Matrix，return ["again","can","dad","dog"].
Example 2:

Input：["a"]，["b"]
Output：[]
Explanation：
 a
search in Matrix，return [].
Challenge
Using trie to implement your algorithm
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string  # 给定一个matrix 和 字典words 求能在矩阵中找到的 字典中的单词
    """

    def init_prefix_set(self, words):
        prefix_set = set()
        for word in words:  # 根据字典的单词 将所有可能的前缀记录到一个set中
            for i in range(len(word)):
                # add all prefix of this word to set
                prefix_set.add(word[: i + 1])
        return prefix_set

    # return all words founded on board according to "dictionary words"
    def wordSearchII(self, board, words):
        if not board:
            return []
        word_set = set(words)
        prefix_set = self.init_prefix_set(words=words)
        result_set = set()
        n, m = len(board), len(board[0])
        # collections.defaultdict(bool)
        visited = [[False] * m for _ in range(n)]
        for i in range(n):  # 从每个点开始做dfs
            for j in range(m):
                visited[i][j] = True
                self.search(
                    board,
                    i,
                    j,
                    board[i][j],
                    word_set=word_set,
                    prefix_set=prefix_set,
                    visited=visited,
                    result_set=result_set,
                )
                visited[i][j] = False
        return list(result_set)

    def search(
        self, board, x, y, word, word_set, prefix_set, visited, result_set
    ):  # 定义: 从x y出发 当前路径上为"word" 找到所有字典中出现的词
        # pruning for invalid word prefix (not in dict)
        if word not in prefix_set:
            return  # word: the word found in current dfs path, visited: visited point in current path
        # if found a word, record it and continue(do not return) because there maybe other word with same prefix
        if word in word_set:
            result_set.add(word)
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_x, new_y = x + dx, y + dy
            # pruning for invalid points or visited points
            if not self.inside(board, new_x, new_y) or visited[new_x][new_y]:
                continue
            # recurse on sub-problem by dfs
            visited[new_x][new_y] = True
            self.search(
                board,
                new_x,
                new_y,
                word + board[new_x][new_y],
                word_set,
                prefix_set,
                visited,
                result_set,
            )
            # backtracking last move to try on new move
            visited[new_x][new_y] = False

    # check if a point is inside board
    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
