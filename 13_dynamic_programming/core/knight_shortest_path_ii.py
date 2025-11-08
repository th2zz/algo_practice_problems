# 4 previous pos offsets
import sys

DIRECTIONS = [(-1, -2), (1, -2), (-2, -1), (2, -1)]


class Solution:
    """https://www.lintcode.com/problem/630/?_from=collection&fromId=161
Medium
Accepted Rate
44%
Given a knight in a chessboard n * m (a binary matrix with 0 as empty and 1 as barrier).
the knight initial position is (0, 0) and he wants to reach position (n - 1, m - 1),
Knight can only be from left to right.
Find the shortest path to the destination position, return the length of the route. Return -1 if knight can not reached.

If the knight is at (x, y), he can get to the following positions in one step:
(x + 1, y + 2)
(x - 1, y + 2)
(x + 2, y + 1)
(x - 2, y + 1)
Example
Example 1:

Input:
[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
Output:
3
Explanation:
[0,0]->[2,1]->[0,2]->[2,3]
Example 2:

Input:
[[0,1,0],[0,0,1],[0,0,0]]
Output:
-1
Tags
Breadth First Search/BFS
Dynamic Programming/DP
Coordinate DP
Company
Amazon
nxm棋盘上 骑士从0,0出发目标到达右下角n-1,m-1 只能从左到右走, 找到最短路径, 返回路径 返回-1如果无法到达
棋盘上0是empty 1是barrier
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """

    def shortestPath2(self, grid):
        if not grid or not grid[0]:  # empty or no cols
            return -1
        n, m = len(grid), len(grid[0])
        dp = [[float('inf')] * 3 for _ in range(n)]  # unreachable except (0, 0), set shortest path to max;   n*3 table
        dp[0][0] = 0  # shortest path to x, y
        for j in range(1, m):  # 只在外层循环变量滚动 滚动size为依赖范围
            for i in range(n):
                dp[i][j % 3] = float('inf')  # 滚动做法在重复利用之前的空间 所以需要这行reset
                if grid[i][j]:  # skip obstacle
                    continue
                for dx, dy in DIRECTIONS:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m:  # 在i, j的最短路径 = min(当前在i, j的路径长, 之前可能正在的位置 + 1步)
                        dp[i][j % 3] = min(dp[i][j % 3], dp[x][y % 3] + 1)
        if dp[n - 1][(m - 1) % 3] == float('inf'):
            return -1
        return dp[n - 1][(m - 1) % 3]

    def shortestPath2_(self, grid):  # 非滚动版本
        if not grid or not grid[0]:
            return -1
        n, m = len(grid), len(grid[0])
        # state: f[i][j] 代表从 0,0 跳到 i,j 的最少步数
        f = [[sys.maxsize for _ in range(m)] for _ in range(n)]
        # initialize: f[0][0] 是起点
        f[0][0] = 0
        # function
        for j in range(m):
            for i in range(n):
                if grid[i][j]:  # skip barrier
                    continue
                for delta_x, delta_y in DIRECTIONS:  # x,y 可以从哪些位置到达本点    f[i][j] = min(所有可行的方案, f[i][j])
                    prev_x, prev_y = i + delta_x, j + delta_y  # 之前的y offset一定为负数 依赖更小的y y需要从小遍历; x offset可正可负
                    if 0 <= prev_x < n and 0 <= prev_y < m:
                        f[i][j] = min(f[i][j], f[prev_x][prev_y] + 1)
        if f[n - 1][m - 1] == sys.maxsize:
            return -1
        return f[n - 1][m - 1]
