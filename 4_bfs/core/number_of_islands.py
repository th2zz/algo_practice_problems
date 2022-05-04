import collections
from typing import List

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution:
    """https://leetcode.cn/problems/number-of-islands/
        https://www.lintcode.com/problem/433/?_from=collection&fromId=161
    Algorithms
    Easy
    Accepted Rate
    36%

    Description
    Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island.
    If two 1 is adjacent, we consider them in the same island.
    We only consider up/down/left/right adjacent.

    Find the number of islands.

    Example
    Example 1:

    Input:
    [
      [1,1,0,0,0],
      [0,1,0,0,1],
      [0,0,0,1,1],
      [0,0,0,0,0],
      [0,0,0,0,1]
    ]
    Output:
    3
    Example 2:

    Input:
    [
      [1,1]
    ]
    Output:
    1
    Tags
    Breadth First Search/BFS
    Union Find
    Related Problems
    860
    Number of Distinct Islands
    Medium
    804
    Number of Distinct Islands II
    Hard
    677
    Number of Big Islands
    Medium
    663
    Walls and Gates
    Medium
    477
    Surrounded Regions
    Medium
    434
    Number of Islands II
    Medium
    连通块数量
        @param grid: a boolean 2D matrix
        @return: an integer
    """

    def numIslands(self, grid: List[List[bool]]) -> int:
        if not grid or not grid[0]:
            return 0
        visited = set()
        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1" and (x, y) not in visited:
                    self.bfs(grid, x, y, visited)
                    res += 1
        return res

    def bfs(self, grid, start_x, start_y, visited):
        q = collections.deque([(start_x, start_y)])
        visited.add((start_x, start_y))
        while q:
            x, y = q.popleft()
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) not in visited and self.is_valid(
                    next_x, next_y, grid
                ):
                    visited.add((next_x, next_y))
                    q.append((next_x, next_y))

    def is_valid(self, x, y, grid):
        m, n = len(grid), len(grid[0])
        return (
            x in range(m) and y in range(n) and grid[x][y] == "1"
        )  # inbound and is on land
