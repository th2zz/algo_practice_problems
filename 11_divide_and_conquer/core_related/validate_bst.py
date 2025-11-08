from lintcode import TreeNode

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """ https://www.lintcode.com/problem/95/?_from=collection&fromId=161
    medium
    Description
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A single node tree is a BST
Example
Example 1:

Input:

tree = {-1}
Output:

true
Explanation:

For the following binary tree（only one node）:
              -1
This is a binary search tree.
Example 2:

Input:

tree = {2,1,4,#,#,3,5}
Output:

true
Explanation:

For the following binary tree:
          2
         / \
        1   4
           / \
          3   5
This is a binary search tree.
Tags
Depth First Search/DFS
Binary Tree
Divide and Conquer
Binary Search Tree
Related Problems
701
Trim a Binary Search Tree
Medium
691
Recover Binary Search Tree
Medium
448
Inorder Successor in BST
Medium
93
Balanced Binary Tree
Easy
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def inorder_traversal(self, root):
        it = BSTIterator(root)
        res = []
        while it.has_next():
            node = it.next()
            res.append(node)
        return res

    def is_valid_b_s_t(self, root: TreeNode) -> bool:
        inorder = self.inorder_traversal(root)
        for i, node in enumerate(inorder):
            if i > 0:
                # bst inorder 不下降序列 但本体规定bst里没有= 左边< 右边> 故需要为严格单增序列
                if node.val <= inorder[i - 1].val:
                    return False
        return True


class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.push_leftmost_branch(root)

    def push_leftmost_branch(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        node = self.stack.pop()
        if node.right:
            self.push_leftmost_branch(root=node.right)
        return node

    def has_next(self):
        return bool(self.stack)
