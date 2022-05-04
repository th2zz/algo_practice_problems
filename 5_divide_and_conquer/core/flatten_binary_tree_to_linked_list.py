"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """ https://www.lintcode.com/problem/453/?_from=collection&fromId=161
    Description
Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.

Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.

Example
Example 1:

Input:{1,2,5,3,4,#,6}
Output：{1,#,2,#,3,#,4,#,5,#,6}
Explanation：
     1
    / \
   2   5
  / \   \
 3   4   6

1
\
 2
  \
   3
    \
     4
      \
       5
        \
         6
Example 2:

Input:{1}
Output:{1}
Explanation：
         1
         1
Challenge
Do it in-place without any extra memory.
经典分治 解决左右半边后 merge solution root接向左子树接向右子树  最后返回当前子树last节点
base case: root == None return None
flatten左子树并获取last node
flatten右子树并获取last node
如果left_last存在
    left_last.right = root.right
    root.right = left_last.head
    root.left = None
return right_last or left_last or root
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def flatten(self, root):  # flatten and return last node
        if not root:
            return root
        # flatten left and right subtree and get last node
        left_last = self.flatten(root.left)
        right_last = self.flatten(root.right)
        if left_last:  # need to transplant flattened left subtree to root
            left_last.right = root.right
            root.right = root.left
            root.left = None
        return right_last or left_last or root
        # tree at root got flattened, return last node of this tree: logically, priority gives to right last, left last, and finally root
