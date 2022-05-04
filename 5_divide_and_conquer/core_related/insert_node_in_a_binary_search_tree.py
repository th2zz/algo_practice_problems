"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """ https://www.lintcode.com/problem/85/?_from=collection&fromId=161
    easy
    Description
Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.

You can assume there is no duplicate values in this tree + node.

Example
Example 1:

Input:

tree = {}
node= 1
Output:

{1}
Explanation:

Insert node 1 into the empty tree, so there is only one node on the tree.

Example 2:

Input:

tree = {2,1,4,#,#,3}
node = 6
Output:

{2,1,4,#,#,3,6}
Explanation:

     2                              2
/   \                          /   \
1     4          -->       1       4
/                                /  \
3                                3      6

Challenge
Can you do it without recursion?

    Binary Tree
Divide and Conquer
Binary Search Tree
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        if not root:
            return node
        curr = root
        while curr != node:
            if node.val < curr.val:
                if not curr.left:
                    curr.left = node
                curr = curr.left
            elif node.val > curr.val:
                if not curr.right:
                    curr.right = node
                curr = curr.right
        return root
