import sys

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
    """  https://www.lintcode.com/problem/597/?_from=collection&fromId=161
    Easy
Description
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum average.

Example
Example 1

Input：
{1,-5,11,1,2,4,-2}
Output：11
Explanation:
The tree is look like this:
     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2
The average of subtree of 11 is 4.3333, is the maximun.
Example 2

Input：
{1,-5,11}
Output：11
Explanation:
     1
   /   \
 -5     11
The average of subtree of 1,-5,11 is 2.3

Tags
Depth First Search/DFS
Binary Tree
Divide and Conquer
Company
Amazon
Related Problems
632
Binary Tree Maximum Node
Easy
628
Maximum Subtree
Easy
596
Minimum Subtree
Easy

    @param root: the root of binary tree
    @return: find the subtree with the maximum average and return its root
    """

    def find_subtree2(self, root: TreeNode) -> TreeNode:
        return self.find_max_avg(root)[1]

    def find_max_avg(self, root):
        if not root:
            return -sys.maxsize, root, 0, 0  # max avg, max avg root, curr sum, number of nodes
        left_max_avg, left_max_avg_root, left_sum, left_nodes = self.find_max_avg(root.left)
        right_max_avg, right_max_avg_root, right_sum, right_nodes = self.find_max_avg(root.right)
        curr_sum = left_sum + right_sum + root.val
        num_nodes = left_nodes + right_nodes + 1
        curr_avg = curr_sum / num_nodes
        curr_max_avg = max(curr_avg, left_max_avg, right_max_avg)
        if curr_max_avg == left_max_avg:
            return left_max_avg, left_max_avg_root, curr_sum, num_nodes
        if curr_max_avg == right_max_avg:
            return right_max_avg, right_max_avg_root, curr_sum, num_nodes
        return curr_max_avg, root, curr_sum, num_nodes
