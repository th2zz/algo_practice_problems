class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
Definition of TreeNode:

"""
"""
Description
Given a root of Binary Search Tree with unique value for each node. Remove the node with given value. If there is no such a node with given value in the binary search tree, do nothing. You should keep the tree still a binary search tree after removal.

Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)


Example
Example 1:

Input:

Tree = {5,3,6,2,4}
value = 3
Output:

{5,2,6,#,4} or {5,4,6,2}
Explanation:

Given binary search tree:
    5
   / \
  3   6
 / \
2   4
Remove 3, you can either return:
    5
   / \
  2   6
   \
    4
or
    5
   / \
  4   6
 /
2
Example 2:

Input:

Tree = {5,3,6,2,4}
value = 4
Output:

{5,3,6,2}
Explanation:

Given binary search tree:
    5
   / \
  3   6
 / \
2   4
Remove 4, you should return:
    5
   / \
  3   6
 /
2
Tags
Binary Tree
Divide and Conquer
Binary Search Tree
Related Problems
85
Insert Node in a Binary Search Tree
Easy
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def remove_node(self, root: TreeNode, value: int) -> TreeNode:
        pass
