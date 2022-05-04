from typing import (
    List,
)


class Solution:
    """ easy
    https://www.lintcode.com/problem/115/?_from=collection&fromId=161
    Description
Follow up for "Unique Paths":
A robot is located at the top-left corner of a m x nmxn grid.

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

1≤n≤100
1≤m≤100

Example
Example 1:

Input:

obstacleGrid = [[0]]
Output:

1
Explanation:

There's only one point

Example 2:

Input:

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output:

2
Explanation:

Only 2 different path
    @param obstacle_grid: A list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        # 获取网格的长宽
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        if n == 0 and m == 0:
            return 0
        dp = [[0] * m for _ in range(n)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        for i in range(0, n):
            for j in range(0, m):
                if i == 0 and j == 0:
                    continue
                # 若遇到障碍物，则跳过
                if obstacleGrid[i][j] == 1:
                    continue
                # 对于上边界，第一个障碍物或边界左边的所有边界点皆可到达
                if i == 0:
                    dp[i][j] = dp[i][j - 1]
                    continue
                # 对于左边界，第一个障碍物或边界前的所有边界点皆可到达
                if j == 0:
                    dp[i][j] = dp[i - 1][j]
                    continue
                # 到达当前点的路径数等于能到达此点上面的点和左边点的路径数之和
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n - 1][m - 1]

#
# res = Solution().unique_paths_with_obstacles([[0, 0, 0],
#                                               [0, 1, 0],
#                                               [0, 0, 0]])
# print(res)
#
# x = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#      [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#      [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#      [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
# x = [[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#      [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
#      [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # 7515305
# res = Solution().unique_paths_with_obstacles(x)
# print(res)
