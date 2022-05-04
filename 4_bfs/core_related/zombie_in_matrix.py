import collections
from typing import (
    List,
)


class Solution:
    """https://www.lintcode.com/problem/598/?_from=collection&fromId=161
    Medium
Give a two-dimensional grid, each grid has a value, 2 for wall, 1 for zombie, 0 for human (numbers 0, 1, 2).
Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall.
How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.

Example
Example 1:

Input:
[[0,1,2,0,0],
 [1,0,0,2,1],
 [0,1,0,0,0]]
Output:
2
Example 2:

Input:
[[0,0,0],
 [0,0,0],
 [0,0,1]]
Output:
4
Tags
Breadth First Search/BFS
Related Problems
573
Build Post Office II
多源点bfs (多个起点最初同时入队) 多少步感染全部(无路可走时)
https://leetcode-cn.com/problems/rotting-oranges/
    @param grid: a 2D integer grid
    @return: an integer
    """

    def zombie(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        q = collections.deque()
        sum_zombies, sum_walls = 0, 0
        n, m = len(grid), len(grid[0])
        for i in range(n):  # 初始化: 数下zombie个数 wall个数 把zombie坐标和steps 加到队列作为bfs源点
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j, 0))  # node structure: x, y, how many steps from source
                    sum_zombies += 1
                if grid[i][j] == 2:
                    sum_walls += 1
        steps = 0
        while q:
            x, y, steps = q.popleft()
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:  # for each one around zombie
                nx, ny = x + dx, y + dy
                if self.is_valid(nx, ny, grid):  # if it is a valid in-bound person, append to queue and mark as zombie
                    q.append((nx, ny, steps + 1))
                    grid[nx][ny] = 1
                    sum_zombies += 1
        if sum_zombies + sum_walls != n * m:
            return -1
        # for i in range(n):  # if any human left, return -1
        #     for j in range(m):
        #         if grid[i][j] == 0:
        #             return -1
        return steps

    def is_valid(self, nx, ny, grid):
        n = len(grid)
        m = len(grid[0])
        return nx in range(n) and ny in range(m) and grid[nx][ny] == 0
