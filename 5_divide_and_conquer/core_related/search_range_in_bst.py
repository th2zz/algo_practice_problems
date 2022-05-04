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


class Solution:
    """https://www.lintcode.com/problem/11/?_from=collection&fromId=161
    medium
    Given a binary search tree and a range [k1, k2], return node values within a given range in ascending order.

Example
Example 1:

Input:

tree = {5}
k1 = 6
k2 = 10
Output:

[]
Explanation:

No number between 6 and 10

Example 2:

Input:

tree = {20,8,22,4,12}
k1 = 10
k2 = 22
Output:

[12,20,22]
Explanation:

[12,20,22] between 10 and 22

Tags
Depth First Search/DFS
Binary Tree
Divide and Conquer
Binary Search Tree
Related Problems
665
Range Sum Query 2D - Immutable
Medium
14
First Position of Target
Easy
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def inorder(self, root):
        it = BSTIterator(root)
        res = []
        while it.has_next():
            res.append(it.next())
        return res

    def search_range(self, root: TreeNode, k1: int, k2: int) -> List[int]:
        if not root:
            return []
        inorder = self.inorder(root)
        start_index = self.find_first_pos_of_target(inorder, k1)
        end_index = self.find_last_pos_of_target(inorder, k2)
        if start_index == -1 or end_index == -1:
            return []
        return [x.val for x in inorder[start_index: end_index + 1]]

    def find_first_pos_of_target(self, inorder, target):
        start, end = 0, len(inorder) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if inorder[mid].val >= target:
                end = mid
            else:
                start = mid
        if inorder[start].val >= target:
            return start
        if inorder[end].val >= target:
            return end
        return -1

    def find_last_pos_of_target(self, inorder, target):
        start, end = 0, len(inorder) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if inorder[mid].val <= target:
                start = mid
            else:
                end = mid
        if inorder[end].val <= target:
            return end
        if inorder[start].val <= target:
            return start
        return -1


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
