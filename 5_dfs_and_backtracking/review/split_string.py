from typing import (
    List,
)
"""
Algorithms
Medium
Accepted Rate
45%

DescriptionSolutionNotesDiscussLeaderboard
Description
Give a string, you can choose to split the string after one character or two adjacent characters, and make the string to be composed of only one character or two characters. Output all possible results.

Example
Example1

Input: "123"
Output: [["1","2","3"],["12","3"],["1","23"]]
Example2

Input: "12345"
Output: [["1","23","45"],["12","3","45"],["12","34","5"],["1","2","3","45"],["1","2","34","5"],["1","23","4","5"],["12","3","4","5"],["1","2","3","4","5"]]
Tags
Depth First Search/DFS
Related Problems
702
Concatenated String with Uncommon Characters of Two Strings
Easy
582
Word Break II
Hard
107
Word Break
Medium
18
Subsets II
Medium
17
Subsets
Medium
"""
class Solution:
    """
    @param s: a string to be split
    @return: all possible split string array
    """
    def split_string(self, s: str) -> List[List[str]]:
        # write your code here
        pass