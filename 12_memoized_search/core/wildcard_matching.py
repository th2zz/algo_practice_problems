class Solution:
    """https://www.lintcode.com/problem/192/?_from=collection&fromId=161
    HARD
    Description
Implement wildcard pattern matching with support for '?' and '*'.The matching rules are as follows：

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

0 <= |s|, |p| <= 1000
It is guaranteed that 𝑠 only contains lowercase Latin letters and p contains lowercase Latin letters , ? and *

Example
Example 1

Input:
"aa"
"a"
Output: false
Example 2

Input:
"aa"
"aa"
Output: true
Example 3

Input:
"aaa"
"aa"
Output: false
Example 4

Input:
"aa"
"*"
Output: true
Explanation: '*' can replace any string
Example 5

Input:
"aa"
"a*"
Output: true
Example 6

Input:
"ab"
"?*"
Output: true
Explanation: '?' -> 'a' '*' -> 'b'
Example 7

Input:
"aab"
"c*a*b"
Output: false
Tags
Dynamic Programming/DP
Two Sequences DP
Memoization Search
Related Problems
154
Regular Expression Matching
Hard
实现通配符匹配 ?match1个字符 *match0个或更多任意字符 返回是否能够在source中完整匹配pattern
    @param source: A string
    @param pattern: A string includes "?" and "*"
    @return: is Match?
    """

    def isMatch(self, source, pattern):
        if source is None or pattern is None:  # allow ""
            return False
        return self.is_match_helper(source, pattern, 0, 0, {})

    def is_match_helper(self, source, pattern, s_idx, p_idx, memo):
        if (s_idx, p_idx) in memo:  # 这里要用in 不能用get否则会超时
            return memo[(s_idx, p_idx)]
        if s_idx == len(source):  # s用完了 p剩余字符需要全为*才能match
            return self.all_stars(pattern, p_idx)
        if p_idx == len(pattern):  # p用完了 s必须也用完了 才能match
            return s_idx == len(source)
        if pattern[p_idx] == '*':  # *match1个字符 或者 没有match任何字符
            matched = self.is_match_helper(source, pattern, s_idx, p_idx + 1, memo) or self.is_match_helper(source,
                                                                                                            pattern,
                                                                                                            s_idx + 1,
                                                                                                            p_idx, memo)
        else:  # 当前字符对匹配 且 剩余字符串匹配
            matched = self.match_char(source[s_idx], pattern[p_idx]) and self.is_match_helper(source, pattern,
                                                                                              s_idx + 1, p_idx + 1,
                                                                                              memo)
        memo[(s_idx, p_idx)] = matched
        return matched  # TODO 返回值为matched

    def all_stars(self, pattern, p_idx):  # 检查pattern从p_idx开始到最后是否均为star
        for i in range(p_idx, len(pattern)):
            if pattern[i] != '*':
                return False
        return True

    def match_char(self, s, p):
        return s == p or p == '?'
