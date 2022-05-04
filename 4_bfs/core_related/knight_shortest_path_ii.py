# OFFSETS IN 8 DIRECTIONS
from typing import List
import collections

OFFSETS = [
    (-1, 2), (1, 2),
    (2, 1), (-2, 1)
]


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
bfs简单图最短路径 如何记录最短路径: maintain a parent dict     backtrace when finished
https://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search
    @param grid: a chessboard included 0 and 1
    @return: the shortest path 从0,0到右下角
    """

    def shortest_path2(self, grid: List[List[bool]]) -> int:
        if not grid or not grid[0]:
            return -1
        n, m = len(grid), len(grid[0])
        q = collections.deque([(0, 0)])
        distance = {(0, 0): 0}  # TODO init to 0
        while q:
            x, y = q.popleft()
            for dx, dy in OFFSETS:
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) not in distance and self.is_valid(next_x, next_y, grid):
                    distance[(next_x, next_y)] = distance[(x, y)] + 1
                    q.append((next_x, next_y))
        return distance.get((n - 1, m - 1), -1)

    def is_valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])
        return x in range(n) and y in range(m) and grid[x][y] == 0
