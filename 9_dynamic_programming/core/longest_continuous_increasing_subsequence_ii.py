class Solution:
    """https://www.lintcode.com/problem/398/?_from=collection&fromId=161
    Algorithms
Hard
Accepted Rate
39%

DescriptionSolutionNotesDiscussLeaderboard
This topic is a pre-release topic. If you encounter any problems, please contact us via "Problem Correction", and we will upgrade your account to VIP as a thank you.
Description
Given an integer matrix. Find the longest increasing continuous subsequence in this matrix and return the length of it.

The longest increasing continuous subsequence here can start at any position and go up/down/left/right.

Example
Example 1:

Input:
    [
      [1, 2, 3, 4, 5],
      [16,17,24,23,6],
      [15,18,25,22,7],
      [14,19,20,21,8],
      [13,12,11,10,9]
    ]
Output: 25
Explanation: 1 -> 2 -> 3 -> 4 -> 5 -> ... -> 25 (Spiral from outside to inside.)
Example 2:

Input:
    [
      [1, 2],
      [5, 3]
    ]
Output: 4
Explanation: 1 -> 2 -> 3 -> 5
Challenge
Assume that it is a N x M matrix. Solve this problem in O(NM) time and memory.

Tags
Coordinate DP
Memoization Search
Topological Sort
Breadth First Search/BFS
Dynamic Programming/DP
Related Problems
397
Longest Continuous Increasing Subsequence
Easy
    @param matrix: A 2D-array of integers
    @return: length of LCIS in this matrix
    """

    def longestContinuousIncreasingSubsequence2(self, A):
        if not A or not A[0]:
            return 0
        n, m = len(A), len(A[0])  # n by m
        points = []
        for i in range(n):
            for j in range(m):
                points.append((A[i][j], i, j))
        points.sort()  # this is to make what we are looking continuous
        dp = {}  # dp[i][j] = length of LCIS end at pos (i, j)
        for point in points:
            # val, x, y = points[i][0], points[i][1], points[i][2]
            val, key = point[0], (point[1], point[2])
            dp[key] = 1
            for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                x, y = key[0] + dx, key[1] + dy
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                if A[x][y] < val:  # dp[i][j] = max{上下左右LCIS + 1}
                    dp[key] = max(dp[key], dp[(x, y)] + 1)
        return max(dp.values())
