"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
from collections import deque

# OFFSETS IN 8 DIRECTIONS
OFFSETS = [
    (-2, -1), (-2, 1),
    (-1, 2), (1, 2),
    (2, 1), (2, -1),
    (1, -2), (-1, -2),
]


class Solution:
    """https://www.lintcode.com/problem/611/?_from=collection&fromId=161
    TAG: NetEase
    Description
Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position,
find the shortest path to a destination position, return the length of the route.
Return -1 if destination cannot be reached.

source and destination must be empty.
Knight can not enter the barrier.
Path length refers to the number of steps the knight takes.
If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
Example
Example 1:

Input:
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2]
Output: 2
Explanation:
[2,0]->[0,1]->[2,2]
Example 2:

Input:
[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2]
Output:-1
简单图最短路径
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid, source, destination):
        q = collections.deque([(source.x, source.y)])
        distance = {(source.x, source.y): 0}
        while q:
            x, y = q.popleft()
            if (x, y) == (destination.x, destination.y):
                return distance[(x, y)]
            for dx, dy in OFFSETS:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) not in distance and self.is_valid(new_x, new_y, grid):
                    q.append((new_x, new_y))
                    distance[(new_x, new_y)] = distance[(x, y)] + 1
        # unreachable
        return -1

    def is_valid(self, x, y, grid):  # grid[x][y] == 1 if on a barrier, cannot move to barrier
        n, m = len(grid), len(grid[0])
        return x in range(n) and y in range(m) and not grid[x][y]
