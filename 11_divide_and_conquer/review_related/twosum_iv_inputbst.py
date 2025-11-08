"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
"""
Algorithms
Medium
Accepted Rate
50%

DescriptionSolutionNotesDiscussLeaderboard
This topic is a pre-release topic. If you encounter any problems, 
please contact us via "Problem Correction", and we will upgrade your account to VIP as a thank you.
Description
Given a binary search tree and a number n, 
find two numbers in the tree that sums equal to n. Return null if solution cannot be found.

Example
样例1

输入：
{4,2,5,1,3}
3
输出： [1,2] (or [2,1])
解释：
二叉搜索树如下：
    4
   / \
  2   5
 / \
1   3
样例2

输入：
{4,2,5,1,3}
5
输出： [2,3] (or [3,2] or [1,4] or [4,1])
Challenge
Use O(1) extra space.

Tags
Binary Search Tree
Depth First Search/DFS
Binary Tree
Divide and Conquer
Company
Facebook
Google
"""

class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        # write your code here
        pass