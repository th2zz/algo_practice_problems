from typing import (
    Set,
)
"""https://www.lintcode.com/problem/624/?fromId=161&_from=collection
Algorithms
Medium
Accepted Rate
40%

DescriptionSolutionNotesDiscussLeaderboard
Description
Given a string s and a set of n substrings. You are supposed to remove every instance of those n substrings from s so that s is of the minimum length and output this minimum length.

Example
Example 1:

Input:
"ccdaabcdbb"
["ab","cd"]
Output:
2
Explanation: 
ccdaabcdbb -> ccdacdbb -> cacdbb -> cabb -> cb (length = 2)
Example 2:

Input:
"abcabd"
["ab","abcd"]
Output:
0
Explanation: 
abcabd -> abcd -> "" (length = 0)
Tags
Breadth First Search/BFS
Company
Amazon
"""
class Solution:
    """
    @param s: a string
    @param dict: a set of n substrings
    @return: the minimum length
    """
    def min_length(self, s: str, dict: Set[str]) -> int:
        # write your code here
        pass