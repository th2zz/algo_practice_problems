class Solution:
    """
    Description
Given a string s, find the longest palindromic subsequence's length in s.
You may assume that the maximum length of s is 1000.

Example
Example1

Input: "bbbab"
Output: 4
Explanation:
One possible longest palindromic subsequence is "bbbb".
Example2

Input: "bbbbb"
Output: 5
Tags
Company
Uber
Amazon
Related Problems
775
Palindrome Pairs
Hard
738
Count Different Palindromic Subsequences
Hard
678
Shortest Palindrome
Medium
200
Longest Palindromic Substring
Medium

    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    bbbab res bbbb 4
    bbbbb res bbbbb 5
    brute force O(n * 2^n)
    https://leetcode-cn.com/problems/longest-palindromic-subsequence/solution/zi-xu-lie-wen-ti-tong-yong-si-lu-zui-chang-hui-wen/
    """
    def longestPalindromeSubseq(self, s):
        if not s:
            return 0
        elif len(s) == 1:
            return 1
        n = len(s)
        length = [[0] * n for _ in range(n)]  # length[i][j] := 从i到j的longest palindromic subseq length
        for i in range(n - 1, -1, -1):
            length[i][i] = 1
            for j in range(i + 1, n):  # length >= 2
                if s[i] == s[j]:
                    length[i][j] = length[i + 1][j - 1] + 2  # 新增两个字符 如果相等 则为之前状态+2
                else:
                    length[i][j] = max(length[i + 1][j], length[i][j - 1])  # 不等 为 max(去掉其中之一字符的解)
        return length[0][n - 1]

    def longest_palindrome_subseq(self, s: str) -> int:
        # len(s) = 0 or 1 return 1
        # for len(s) == 2 return 2 if s[0] == s[1] else 1
        # for len(s) >= 3
        # len_lps[i...j] lps for substr at i to j
        # len_lps[i...j] = 2 + len_lps[i + 1 ... j - 1] if char at i == char at j
        # otherwise len_lps[i...j] = max(len_lps[i + 1...j], len_lps[i...j - 1]
        # 2d dp i depends on larger i, j smaller j
        if not s:
            return 0
        elif len(s) == 1:
            return 1
        # for n >= 3
        n = len(s)
        len_lps = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                len_lps[i][j] = 1
                if j < i:
                    len_lps[i][j] = 0
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    len_lps[i][j] = 2 + len_lps[i + 1][j - 1]
                else:
                    len_lps[i][j] = max(len_lps[i + 1][j], len_lps[i][j - 1])
        return len_lps[0][n - 1]

a = Solution().longest_palindrome_subseq('bbbb')
b = Solution().longest_palindrome_subseq('abb')
print(a)
print(b)