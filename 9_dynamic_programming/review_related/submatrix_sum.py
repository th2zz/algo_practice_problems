from typing import (
    List,
)
"""
Algorithms
Medium
Accepted Rate
36%

DescriptionSolutionNotesDiscussLeaderboard
Description
Given an integer matrix, find a submatrix where the sum of numbers is zero. Your code should return the coordinate of the left-up and right-down number.

If there are multiple answers, you can return any of them.

Example
Example 1:

Input:
[
  [1, 5, 7],
  [3, 7, -8],
  [4, -8 ,9]
]
Output: [[1, 1], [2, 2]]
Example 2:

Input:
[
  [0, 1],
  [1, 0]
]
Output: [[0, 0], [0, 0]]
Challenge
O(n3) time.

Tags
Prefix Sum Array
Array
Related Problems
944
Maximum Submatrix
Medium
139
Subarray Sum Closest
Medium
138
Subarray Sum
Easy
"""

class Solution:
    """
    @param matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """
    def submatrix_sum(self, matrix: List[List[int]]) -> List[List[int]]:
        # write your code here
        pass