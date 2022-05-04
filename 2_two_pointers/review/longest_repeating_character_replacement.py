class Solution:
    """https://www.lintcode.com/problem/1246/?fromId=161&_from=collection
Algorithms
Medium
Accepted Rate
45%

DescriptionSolutionNotesDiscussLeaderboard
Description
Given a string that consists of only uppercase English letters,
you can replace any letter in the string with another letter at most k times.
Find the length of a longest substring containing all repeating letters
you can get after performing the above operations.



Both the string's length and k will not exceed 10^4.

Example
Example1

Input:
"ABAB"
2
Output:
4
Explanation:
Replace the two 'A's with two 'B's or vice versa.
Example2

Input:
"AABABBA"
1
Output:
4
Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
Tags
Hash Table
Same Direction Two Pointers
Two Pointers
Company
Pocket Gems
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    def character_replacement(self, s: str, k: int) -> int:
        pass