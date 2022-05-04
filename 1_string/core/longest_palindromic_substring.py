class Solution:
    """https://www.lintcode.com/problem/200/?_from=collection&fromId=161
    is_palindrome[i][j] substring [i...j] is palindrome
base case: length 1, 2
is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j] for length >= 3

Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.

Example
Example 1:

Input:"abcdzdcab"
Output:"cdzdc"
Example 2:

Input:"aba"
Output:"aba"
Challenge
O(n2) time is acceptable. Can you do it in O(n) time.

Tags
Company
Amazon
Microsoft
Bloomberg
Uber
Related Problems
916
Palindrome Permutation
Easy
893
Longest Palindromic Substring II
Hard
775
Palindrome Pairs
Hard
667
Longest Palindromic Subsequence
Medium
415
Valid Palindrome
Medium
200
Longest Palindromic Substring
Medium
108
Palindrome Partitioning II
Medium

- 最长回文子串

- Eg. lps("abcdzdcab") = "cdzdc";  lps("aba") = "aba";

- 一个长度为n的字符串的子串(substring)的数量级是O(n^2)

  - substring子串 必须是连续的

    - abcd:     a, b, c, d;    ab, bc, cd;  abc, bcd;  abcd   从长度为1至n共 n+n-1+...+1= (n+1)*n/2个子序列 故O(n^2)

  - subsequence子序列 非连续字符 如ac

    - 子序列不需要是连续的(可以跳跃), 但只能从原序列中删除/不删  不可以旋转   参考LCS最长公共子序列问题
      - A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without
      changing the order of the remaining elements.

    - 因此对于长度为n的字符串的子序列，每个字符都有选或不选两种可能。 因此其子序列的数量是指数级别O(2^n)的  size of power set

    @param s: input string
    @return: a string as the longest palindromic substring
    """

    def longestPalindrome2(self, s):
        if not s or (s and len(s) == 1):  # handle base case n == 0, 1, 2
            return s
        elif len(s) == 2:
            return s[0] if s[0] != s[1] else s
        start_index, max_len, n = 0, 1, len(s)
        is_palindrome = [[False] * n for _ in range(n)]  # deep copy init n x n matrix
        for i in range(n):
            is_palindrome[i][i] = True  # init all length 1 substr
            if i <= n - 2:
                is_palindrome[i][i + 1] = s[i] == s[i + 1]  # init all length 2 substr && record longest substr info
                if is_palindrome[i][i + 1]:
                    start_index, max_len = i, 2
        for i in range(n - 1, -1, -1):  # i依赖于更大的 j依赖于更小的 i从大到小遍历 j从小到大遍历
            for j in range(i + 2, n, 1):  # i,j长度至少为3
                is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]  # when n >= 3
                if is_palindrome[i][j] and j - i + 1 > max_len:
                    start_index, max_len = i, j - i + 1
        return s[start_index: start_index + max_len]

    def longestPalindrome(self, s):  # 枚举长度的解法 需要处理的base case 2不太好想
        if not s:
            return ""
        n = len(s)
        if n == 1:
            return s
        if n == 2:
            return s if s[0] == s[-1] else s[0]
        # deep copy, avoid copied arr points to the same arr
        is_palindrome = [[False] * n for _ in
                         range(n)]  # is_palindrome[i][j] = substring indexed [i...j] is palindromic
        for i in range(n):
            is_palindrome[i][i] = True  # base case 1 char
            if i >= 1:
                is_palindrome[i][i - 1] = True  # base case 2 char 解决长度为2时候 i+1 j-1为空字符串 需要无脑返回True 让s[i] s[j]继续比较
        start_index, max_len = 0, 1
        for length in range(2, n + 1):  # 需要从2开始枚举长度 否则abb这种过不了
            for i in range(n - length + 1):  # 枚举起始位置 计算结束位置 如果是palindrome 记录当前最长长度和start pos
                j = i + length - 1
                is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]
                if is_palindrome[i][j] and length > max_len:
                    max_len = length
                    start_index = i
        return s[start_index: start_index + max_len]  # start: stop
