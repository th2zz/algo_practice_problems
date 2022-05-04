class Solution:
    """https://www.lintcode.com/problem/1375/?fromId=161&_from=collection
Algorithms
Medium
Accepted Rate
47%

DescriptionSolutionNotesDiscussLeaderboard
Description
Given a string S with only lowercase characters.

Return the number of substrings that contains at least k distinct characters.

Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)


10 ≤ length(S) ≤ 1,000,00010≤length(S)≤1,000,000
1 ≤ k ≤ 261≤k≤26
Example
Example 1:

Input: S = "abcabcabca", k = 4
Output: 0
Explanation: There are only three distinct characters in the string.
Example 2:

Input: S = "abcabcabcabc", k = 3
Output: 55
Explanation: Any substring whose length is not smaller than 3 contains a, b, c.
    For example, there are 10 substrings whose length are 3, "abc", "bca", "cab" ... "abc"
    There are 9 substrings whose length are 4, "abca", "bcab", "cabc" ... "cabc"
    ...
    There is 1 substring whose length is 12, "abcabcabcabc"
    So the answer is 1 + 2 + ... + 10 = 55.
Tags
Same Direction Two Pointers
Two Pointers
String
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def k_distinct_characters(self, s: str, k: int) -> int:
        pass