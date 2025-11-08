"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
"""
Algorithms
Medium
Accepted Rate
37%

DescriptionSolutionNotesDiscussLeaderboard
Description
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
The nearest common ancestor of two nodes refers to the nearest common node among all the parent nodes of two nodes (including the two nodes).
Return null if LCA does not exist.

node A or node B may not exist in tree.
Each node has a different value

Example
Example1

Input: 
{4, 3, 7, #, #, 5, 6}
3 5
5 6
6 7 
5 8
Output: 
4
7
7
null
Explanation:
  4
 / \
3   7
   / \
  5   6

LCA(3, 5) = 4
LCA(5, 6) = 7
LCA(6, 7) = 7
LCA(5, 8) = null
Example2

Input:
{1}
1 1
Output: 
1
Explanation:
The tree is just a node, whose value is 1.
Tags
Depth First Search/DFS
Binary Tree
Divide and Conquer
Company
LinkedIn
Facebook
Related Problems
474
Lowest Common Ancestor II
Easy
88
Lowest Common Ancestor of a Binary Tree
Medium
Recommend Courses
"""

class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        pass