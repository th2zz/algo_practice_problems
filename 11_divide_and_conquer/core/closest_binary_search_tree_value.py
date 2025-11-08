"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """ https://www.lintcode.com/problem/900/?_from=collection&fromId=161
    Description
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example
Example1

Input: root = {5,4,9,2,#,8,10} and target = 6.124780
Output: 5
Explanation：
Binary tree {5,4,9,2,#,8,10},  denote the following structure:
        5
       / \
     4    9
    /    / \
   2    8  10
Example2

Input: root = {3,2,4,1} and target = 4.142857
Output: 4
Explanation：
Binary tree {3,2,4,1},  denote the following structure:
     3
    / \
  2    4
 /
1
如果root值 < target 更新lower bound 去右子树 root值 > target 更新upper bound 去左子树 root值==target直接返回 最后返回更近的
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closestValue(self, root, target):  # 根据大小关系非递归查找
        upper_bound, lower_bound = root, root
        while root:
            if root.val < target:  # target比root大 target不可能在左子树 只可能在根结点或右子树 下边界设置为root后去右子树继续探索
                lower_bound = root
                root = root.right
            elif target < root.val:  # 同理
                upper_bound = root
                root = root.left
            else:  # found target at root
                return root.val
        # if not lower_bound:
        #     return upper_bound.val
        # if not upper_bound:
        #     return lower_bound.val
        # 返回最近的值
        return upper_bound.val if abs(upper_bound.val - target) <= abs(lower_bound.val - target) else lower_bound.val

    def closestValueRecursive(self, root, target):
        # recursive solution
        if not root:
            return None
        # 找到小于等于target的最大值 / find {target} Infimum and supremum 上下确界
        lower = self.get_lower_bound(root, target)
        upper = self.get_upper_bound(root, target)
        # handles cases where one is empty
        if not lower:
            return upper.val
        if not upper:
            return lower.val
        # return the one with smallest difference
        if target - lower.val < upper.val - target:
            return lower.val
        return upper.val

    def get_lower_bound(self, root, target):
        if not root:
            return None
        if target < root.val:
            return self.get_lower_bound(root.left, target)
        # root.val <= target, first try to find a closer lower bound in right subtree
        lower = self.get_lower_bound(root.right, target)
        # if found better lower bound, return that one, otherwise return root
        return root if not lower else lower

    def get_upper_bound(self, root, target):
        if not root:
            return None
        if root.val <= target:
            return self.get_upper_bound(root.right, target)
        # root.val > target, first try to find a closer upper bound in left subtree
        upper = self.get_upper_bound(root.left, target)
        # if found better upper bound, return that one, otherwise return root
        return root if not upper else upper
