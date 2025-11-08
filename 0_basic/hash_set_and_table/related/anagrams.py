from typing import (
    List,
)


class Solution:
    """https://www.lintcode.com/problem/171
    Medium
    Description
Given an array of strings, return all groups of strings that are anagrams.
If a string is Anagram,there must be another string with the same letter set but different order in S.

All inputs will be in lower-case

Example
Example 1:

Input:["lint", "intl", "inlt", "code"]
Output:["lint", "inlt", "intl"]
Example 2:

Input:["ab", "ba", "cd", "dc", "e"]
Output: ["ab", "ba", "cd", "dc"]
Challenge
What is Anagram?

Two strings are anagram if they can be the same after change the order of characters.
Tags
Hash Table
String
Related Problems
1038
Jewels And Stones
Easy
813
Find Anagram Mappings
Easy
772
Group Anagrams
Medium
638
Isomorphic Strings
Easy
647
Find All Anagrams in a String
Medium
503
Anagram (Map Reduce)
Medium
158
Valid Anagram
Easy
    @param strs: A list of strings
    @return: A list of strings
             we will sort your return value in output
 找到所有互为anagram的字符串  anagram group含为字符集相同但顺序不同的字符串们
 (找到所有size>=2的anagram组)
    """

    def anagrams(self, strs: List[str]) -> List[str]:
        table = {}  # key: anagram representative sorted str : [strs that are in the same anagram group]
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in table:
                table[sorted_word] = [word]  # init, add word to anagram group
            else:
                table[sorted_word].append(word)  # add to anagram group
        res = []
        for anagram_group in table.values():
            if len(anagram_group) >= 2:  # add anagram group of size >= 2 to res, as required by the question
                res.extend(anagram_group)
        return res
