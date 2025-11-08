"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""
"""
Algorithms
Easy
Accepted Rate
51%

DescriptionSolutionNotesDiscussLeaderboard
Description
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

The lowest common ancestor of two nodes refers to the lowest common node among all the parent nodes of two nodes (including the two nodes).

In addition to the left and right son pointers, each node also contains a father pointer, parent, pointing to its own father.

Example
Example 1:

Input：{4,3,7,#,#,5,6},3,5
Output：4
Explanation：
     4
     / \
    3   7
       / \
      5   6
LCA(3, 5) = 4
Example 2:

Input：{4,3,7,#,#,5,6},5,6
Output：7
Explanation：
      4
     / \
    3   7
       / \
      5   6
LCA(5, 6) = 7
Tags
Binary Tree
Related Problems
578
Lowest Common Ancestor III
Medium
88
Lowest Common Ancestor of a Binary Tree
Medium
Recommend Courses
"""

class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        pass