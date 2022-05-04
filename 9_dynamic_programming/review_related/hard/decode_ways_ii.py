"""
Algorithms
Hard
Accepted Rate
39%

DescriptionSolutionNotesDiscussLeaderboard
Description
A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character *, which can be treated as one of the numbers from 1 to 9.
Given the encoded message containing digits and the character *, return the total number of ways to decode it.
Also, since the answer may be very large, you should return the output mod 10^9 + 7.

The length of the input string will fit in range [1, 10^5].
The input string will only contain the character * and digits 0 - 9.
Example
Example 1

Input: "*"
Output: 9
Explanation: You can change it to "A", "B", "C", "D", "E", "F", "G", "H", "I".
Example 2

Input: "1*"
Output: 18
Tags
Dynamic Programming/DP
Partition DP
Company
Facebook
Related Problems
512
Decode Ways
Medium
"""


class Solution:
    """
    @param s: a message being encoded
    @return: an integer
    """

    def num_decodings(self, s: str) -> int:
        # write your code here
        pass
