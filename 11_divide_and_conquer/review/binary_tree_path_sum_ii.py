from typing import (
    List,
)
from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
"""
Algorithms
Medium
Accepted Rate
40%

DescriptionSolutionNotesDiscussLeaderboard
Description
Given a binary tree and a target value, design an algorithm to find all paths in the binary tree that sum to that target value. The path can start and end at any node, but it needs to be a route that goes all the way down. That is, the hierarchy of nodes on the path is incremented one by one.

Example
Example 1:

Input:
{1,2,3,4,#,2}
6
Output:
[[2, 4],[1, 3, 2]]
Explanation:
The binary tree is like this:
    1
   / \
  2   3
 /   /
4   2
for target 6, it is obvious 2 + 4 = 6 and 1 + 3 + 2 = 6.
Example 2:

Input:
{1,2,3,4}
10
Output:
[]
Explanation:
The binary tree is like this:
    1
   / \
  2   3
 /   
4   
for target 10, there is no way to reach it.
Tags
Depth First Search/DFS
Binary Tree
Divide and Conquer
Related Problems
863
Binary Tree Path Sum IV
Medium
376
Binary Tree Path Sum
Easy
472
Binary Tree Path Sum III
Hard
94
Binary Tree Maximum Path Sum
Medium
Recommend Courses
"""
class Solution:
    """
    @param root: the root of binary tree
    @param target: An integer
    @return: all valid paths
             we will sort your return value in output
    """
    def binary_tree_path_sum2(self, root: TreeNode, target: int) -> List[List[int]]:
        # write your code here
        pass