from typing import (
    List,
)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

"""
Definition of TreeNode:

"""
"""https://www.lintcode.com/problem/901/?fromId=161&_from=collection
901 · Closest Binary Search Tree Value II
Algorithms
Hard
Accepted Rate
49%

Description
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)


Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Example
Example 1:

Input:
{1}
0.000000
1
Output:
[1]
Explanation：
Binary tree {1},  denote the following structure:
 1
Example 2:

Input:
{3,1,4,#,2}
0.275000
2
Output:
[1,2]
Explanation：
Binary tree {3,1,4,#,2},  denote the following structure:
  3
 /  \
1    4
 \
  2
Challenge
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

Tags
Binary Tree
Divide and Conquer
Binary Search Tree
Company
Google
"""
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
             we will sort your return value in output
    """
    def closest_k_values(self, root: TreeNode, target: float, k: int) -> List[int]:
        pass
