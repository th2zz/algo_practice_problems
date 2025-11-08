class Solution:
    """https://www.lintcode.com/problem/109/?_from=collection&fromId=161
    Algorithms
Medium
Accepted Rate
32%

DescriptionSolutionNotesDiscussLeaderboard
Description
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on
the row below.

Bonus point if you are able to do this using only O(n)O(n) extra space, where n is the total number of rows
in the triangle.

Example
Example 1:

Input:

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
Output:

11
Explanation:

The minimum path sum from top to bottom is 11 (2 + 3 + 5 + 1 = 11).

Example 2:

Input:

triangle = [
     [2],
    [3,2],
   [6,5,7],
  [4,4,8,1]
]
Output:

12
Explanation:

The minimum path sum from top to bottom is 12 (2 + 2 + 7 + 1 = 12).

Tags
Dynamic Programming/DP
Coordinate DP
Memoization Search
Related Problems
110
Minimum Path Sum
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        if not triangle or not triangle[0]:
            return -1
        n = len(triangle)
        # dp[x][y]: minimum path sum from top vertex (0,0) to (x,y)
        dp = [[0] * n, [0] * n]
        dp[0][0] = triangle[0][0]  # init
        for i in range(1, n):  # traverse row; only do rolling at each row index access in dp
            # init leftmost pt and rightmost pt on each row
            dp[i % 2][0] = dp[(i - 1) % 2][0] + triangle[i][0]  # dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i % 2][i] = dp[(i - 1) % 2][i - 1] + triangle[i][i]  # dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
            for j in range(1, i):  # traverse col
                # dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
                dp[i % 2][j] = min(dp[(i - 1) % 2][j], dp[(i - 1) % 2][j - 1]) + triangle[i][j]
        return min(dp[(n - 1) % 2])  # 返回最后一层min
