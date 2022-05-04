from typing import (
    List,
)
from lintcode import (
    ParentTreeNode,
)

""" 
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""
"""
Algorithms
Hard
Accepted Rate
53%

DescriptionSolutionNotesDiscussLeaderboard
Description
Give a binary tree, and a target number, find all path that the sum of nodes equal to target, the path could be start and end at any node in the tree.

Example
Example1

Input: {1,2,3,4},6
Output: [[2, 4],[2, 1, 3],[3, 1, 2],[4, 2]]
Explanation:
The tree is look like this:
    1
   / \
  2   3
 /
4
Example2

Input: {1,2,3,4},3
Output: [[1,2],[2,1],[3]]
Explanation:
The tree is look like this:
    1
   / \
  2   3
 /
4
Tags
Depth First Search/DFS
Binary Tree
Divide and Conquer
Related Problems
863
Binary Tree Path Sum IV
Medium
614
Binary Tree Longest Consecutive Sequence II
Medium
376
Binary Tree Path Sum
Easy
246
Binary Tree Path Sum II
Medium
"""
class Solution:
    """
    @param root: the root of binary tree
    @param target: An integer
    @return: all valid paths
             we will sort your return value in output
    """
    def binary_tree_path_sum3(self, root: ParentTreeNode, target: int) -> List[List[int]]:
        # write your code here
        pass
