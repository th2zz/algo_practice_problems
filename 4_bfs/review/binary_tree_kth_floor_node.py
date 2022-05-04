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

class Solution:
    """https://www.lintcode.com/problem/939/?fromId=161&_from=collection
Algorithms
Medium
Accepted Rate
80%

DescriptionSolutionNotesDiscussLeaderboard
Description
Return the number of nodes in the kth layer(The layer number starts from 1 and the root node is layer 1).

Example
Example1

Input: root = {3,9,20,#,#,15,7}, k = 2
Output: 2
Explanation:
  3
 / \
9  20
  /  \
 15   7
Example2

Input: root = {3,1,2}, k = 1
Output: 1
Explanation:
  3
 / \
1   2
Tags
Depth First Search/DFS
Binary Tree
Breadth First Search/BFS
    @param root: the root node
    @param k: an integer
    @return: the number of nodes in the k-th layer of the binary tree
    """
    def kthfloor_node(self, root: TreeNode, k: int) -> int:
        # Write your code here
        pass
