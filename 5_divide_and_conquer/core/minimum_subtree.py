"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys


class Solution:
    """ https://www.lintcode.com/problem/596/?_from=collection&fromId=161
    Description
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.
The range of input and output data is in int.

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.

Example
Example 1:

Input:
{1,-5,2,1,2,-4,-5}
Output:1
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
1   2 -4  -5
The sum of whole tree is minimum, so return the root.
Example 2:

Input:
{1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.

    @param root: the root of binary tree
    @return: the root of the minimum subtree 找到和最小的子树并返回根节点
    """

    def findSubtree(self, root):
        _, min_subtree_root, _ = self.get_min_sum_tree(root)
        return min_subtree_root

    def get_min_sum_tree(self, root):
        if not root:  # return 最小子树和 最小子树根 当前子树和
            return sys.maxsize, None, 0  # curr min_sum, curr min_sum root, curr sum
        left_min, left_subtree, left_curr_sum = self.get_min_sum_tree(root.left)
        right_min, right_subtree, right_curr_sum = self.get_min_sum_tree(root.right)
        curr_sum = left_curr_sum + root.val + right_curr_sum  # TODO 当前子树和为 左右当前子树和 + 本身root.val
        min_sum = min(left_min, right_min, curr_sum)  #  当前最小子树和为三者最小
        if left_min == min_sum:  # case 1. left subtree sum is minimum
            return left_min, left_subtree, curr_sum
        if right_min == min_sum:  # case 2. right subtree sum is minimum
            return right_min, right_subtree, curr_sum
        return curr_sum, root, curr_sum  # case 3. current tree sum is minimum
