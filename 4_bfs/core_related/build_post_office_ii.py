from typing import (
    List,
)
"""
Algorithms
Hard
Accepted Rate
37%
Given a 2D grid, each cell is either a wall 2, an house 
1 or empty 0 (the number zero, one, two), find a place 
to build a post office so that the sum of the distance from the post office to all the houses is smallest.

Returns the sum of the minimum distances from all houses to the post office.Return -1 if it is not possible.

You cannot pass through wall and house, but can pass through empty.
You only build post office on an empty.
Example
Example 1:

Input：[[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]
Output：8
Explanation： Placing a post office at (1,1), the distance that post office to all the house sum is smallest.
Example 2:

Input：[[0,1,0],[1,0,1],[0,1,0]]
Output：4
Explanation： Placing a post office at (1,1), the distance that post office to all the house sum is smallest.
Tags
Enumerate
Breadth First Search/BFS
Company
Zenefits
Google
Related Problems
803
Shortest Distance from All Buildings
Hard
663
Walls and Gates
Medium
598
Zombie in Matrix
Medium
574
Build Post Office
Medium
Recommend Courses
"""
class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortest_distance(self, grid: List[List[int]]) -> int:
        pass
