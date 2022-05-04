class Solution:
    """https://www.lintcode.com/problem/627/?_from=collection&fromId=161
        Description
    Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be
    built with those letters.

    This is case sensitive, for example "Aa" is not considered a palindrome here.

    Assume the length of given string will not exceed 100000.

    Example
    Example 1:

    Input : s = "abccccdd"
    Output : 7
    Explanation :
    One longest palindrome that can be built is "dccaccd", whose length is `7`.
    Tags
    Hash Table
    Company
    Google
    Amazon
    Related Problems
    916
    Palindrome Permutation
    Easy
    891
    Valid Palindrome II
    Medium
    745
    Palindromic Ranges
    Medium
    678
    Shortest Palindrome
    Medium
    415
    Valid Palindrome
    Medium

        @param s: a string which consists of lowercase or uppercase letters
        @return: the length of the longest palindromes that can be built with these letters
        给定一个字符串 找到使用其中字符可构建最长回文的长度
    """

    def longestPalindrome(self, s):
        # aebbbccccdd  create a frequency table
        # a: 1
        # e: 1
        # b: 3
        # c: 4
        # d: 2
        # 取最大的奇数频数 + 所有偶数频数相加 + 其他奇数频数均少取一个(构成偶数)
        # 相当于 整个字符串长度 - 奇数频数 + 1  代表所有奇数除了出现次数最多那个均少取1个构成对称
        if not s:
            return 0
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1  # O(n) get frequency table
        oddcnt = 0
        for c, fcnt in freq.items():
            if fcnt % 2 == 1:
                oddcnt += 1
        return len(s) if oddcnt < 1 else len(s) - oddcnt + 1


# print(Solution().longestPalindrome("bb"))
