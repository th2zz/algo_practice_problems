from typing import (
    List,
)
"""
Description
Given a matrix of lower alphabets and a dictionary. Find maximum number of words in the dictionary that can be found in the matrix at the same time. A word can start from any position in the matrix and go left/right/up/down to the adjacent position. One character only be used once in the matrix. No same word in dictionary

Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)


Example
Example 1:

Input：
["doaf","agai","dcan"]，["dog","dad","dgdg","can","again"]
Output：
2
Explanation：
  d o a f
  a g a i
  d c a n
search in Matrix, you can find `dog` and `can` in the meantime.
Example 2:

Input：
["a"]，["b"]
Output：
0
Explanation：
 a
search in Matrix，return 0.
Tags
Hash Table
Depth First Search/DFS
Trie

"""
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: return the maximum nunber
    """
    def word_search_i_i_i(self, board: List[List[str]], words: List[str]) -> int:
        pass
