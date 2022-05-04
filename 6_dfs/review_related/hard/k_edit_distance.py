from typing import (
    List,
)
"""
Algorithms
Hard
Accepted Rate
39%

Description
Given a set of strings which just has lower case letters and a target string, 
output all the strings for each the edit distance with the target no greater than k.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example
Example 1:

Given words = `["abc", "abd", "abcd", "adc"]` and target = `"ac"`, k = `1`
Return `["abc", "adc"]`
Input:
["abc", "abd", "abcd", "adc"]
"ac"
1
Output:
["abc","adc"]

Explanation:
"abc" remove "b"
"adc" remove "d"
Example 2:

Input:
["acc","abcd","ade","abbcd"]
"abc"
2
Output:
["acc","abcd","ade","abbcd"]

Explanation:
"acc" turns "c" into "b"
"abcd" remove "d"
"ade" turns "d" into "b" turns "e" into "c"
"abbcd" gets rid of "b" and "d"
Tags
Depth First Search/DFS
Two Sequences DP
Trie
Dynamic Programming/DP
Company
Airbnb
Google
Related Problems
635
Boggle Game
Hard
634
Word Squares
Hard
473
Add and Search Word - Data structure design
Medium
442
Implement Trie (Prefix Tree)
Medium
119
Edit Distance
Medium
Recommend Courses
"""
class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
             we will sort your return value in output
    """
    def k_distance(self, words: List[str], target: str, k: int) -> List[str]:
        # write your code here
        pass