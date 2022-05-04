class Solution:  # https://leetcode.cn/problems/longest-common-subsequence/
    """
    Given two strings text1 and text2, return the length of their longest common subsequence. 
    If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        m, n = len(text1), len(text2)
        # dp[i][j]:= len(LCS(text1[:i], text2[:j]))
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                c1, c2 = text1[i - 1], text2[j - 1]
                if c1 == c2:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # drop 1 character from text1, or text2 to find lcs
        return dp[m][n]
