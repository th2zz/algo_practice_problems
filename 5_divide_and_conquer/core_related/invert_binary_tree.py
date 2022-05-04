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
    """https://www.lintcode.com/problem/175/?_from=collection&fromId=161
    easy
    Invert a binary tree.Left and right subtrees exchange.
    Example
Example 1:

Input: {1,3,#}
Output: {1,#,3}
Explanation:
	  1    1
	 /  =>  \
	3        3
Example 2:

Input: {1,2,3,#,#,4}
Output: {1,3,2,#,4}
Explanation:

      1         1
     / \       / \
    2   3  => 3   2
       /       \
      4         4
Challenge
Do it in recursion is acceptable, can you do it without recursion?
TAGS
Depth First Search/DFS
Binary Tree
Divide and Conquer
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def invert_binary_tree(self, root: TreeNode):
        return self.invert_helper(root)

    def invert_helper(self, root):
        if not root:
            return root
        inverted_left = self.invert_helper(root.left)
        inverted_right = self.invert_helper(root.right)
        root.left, root.right = inverted_right, inverted_left
        return root
