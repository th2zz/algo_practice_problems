from typing import (
    List,
)
"""https://www.lintcode.com/problem/110/?fromId=161&_from=collection
Algorithms
Easy
Accepted Rate
45%

DescriptionSolutionNotesDiscussLeaderboard
Description
Given a m * nm∗n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)


The robot can only move either down or right at any point in time.

Example
Example 1:

Input:

grid = [[1,3,1],[1,5,1],[4,2,1]]
Output:

7
Explanation:

Path is: 1 -> 3 -> 1 -> 1 -> 1

Example 2:

Input:

grid = [[1,3,2]]
Output:

6
Explanation:

Path is: 1 -> 3 -> 2

Tags
Dynamic Programming/DP
Coordinate DP
Related Problems
1682
Minimum Path Sum III
Easy
1058
Cherry Pickup
Hard
794
Sliding Puzzle II
Hard
109
Triangle
Medium
94
Binary Tree Maximum Path Sum
Medium
"""
class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def min_path_sum(self, grid: List[List[int]]) -> int:
        pass
