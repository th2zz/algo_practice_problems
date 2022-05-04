from typing import (
    List,
    Set,
)
"""
Description
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end.
Transformation rule such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)


All words have the same length.
All words contain only lowercase alphabetic characters.
At least one solution exists.
The number of words is less than or equal to 10000
The word length is less than or equal to 10
Example
Example 1:

Input:

start = "a"
end = "c"
dict =["a","b","c"]
Output:

[["a","c"]]
Explanation:

"a"->"c"

Example 2:

Input:

start ="hit"
end = "cog"
dict =["hot","dot","dog","lot","log"]
Output:

[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation:

1."hit"->"hot"->"dot"->"dog"->"cog"
2."hit"->"hot"->"lot"->"log"->"cog"

Tags
Depth First Search/DFS
Breadth First Search/BFS
Related Problems
790
Parser
Medium
120
Word Ladder
Hard
"""
class Solution:

    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: a list of lists of string
             we will sort your return value in output
    """
    def find_ladders(self, start: str, end: str, dict: Set[str]) -> List[List[str]]:
        pass