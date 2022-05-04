"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """ https://www.lintcode.com/problem/902/?_from=collection&fromId=161
    Description
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example
Example 1:

Input：{1,#,2},2
Output：2
Explanation：
	1
	 \
	  2
The second smallest element is 2.
Example 2:

Input：{2,1,3},1
Output：1
Explanation：
  2
 / \
1   3
The first smallest element is 1.
Challenge
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
How would you optimize the kthSmallest routine?
本题重点掌握如何实现bst inorder iterator
非递归二叉树遍历
重点掌握中序遍历
前序遍历可能考察
后序遍历一般不要求 能递归实现即可 因为实际上是分治
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root, k):  # k-1次next后 返回it.next()
        it = BSTIterator(root)
        for _ in range(k - 1):
            it.next()
        return it.next().val

    def inorderTraversal(self, root):  # while has next, append next() to res
        it = BSTIterator(root)
        res = []
        while it.hasNext():
            res.append(it.next().val)
        return res

    # def inorderTraversal0(self, root):  # without dummy 这样省掉了开始的push left most branch
    #     stack = []
    #     BSTIterator.push_leftmost_branch(root, stack)  # init stack
    #     res = []
    #     while stack:
    #         node = BSTIterator.get_next(stack)
    #         res.append(node.val)
    #     return res

    # def kthSmallest0(self, root, k):  # without dummy
    #     stack = []
    #     BSTIterator.push_leftmost_branch(root, stack)  # init stack
    #     for _ in range(k - 1):  # TODO b相比st iterator新增的一行: 做k - 1次 .get_next操作
    #         BSTIterator.get_next(stack)
    #     return stack[-1].val  # 最后栈顶元素即为结果

    # def kthSmallest1(self, root, k):  # with dummy 这样省掉了开始的push left most branch
    #     dummy = TreeNode(-1)
    #     dummy.right = root
    #     stack = [dummy]
    #     for i in range(k):  # DIFFERENT
    #         BSTIterator.get_next(stack)
    #         # if not stack:
    #         #     return None  # 用完了 无法获取kth smallest
    #         # if stack:  # 如果要记录中序遍历结果 这里记录当前栈顶元素
    #         #     inorder.append(stack[-1].val)
    #     return stack[-1].val
    #
    # def inorderTraversal1(self, root):  # with dummy 这样省掉了开始的push left most branch
    #     dummy = TreeNode(-1)
    #     dummy.right = root
    #     stack = [dummy]
    #     res = []
    #     while stack:
    #         BSTIterator.get_next(stack)
    #         if stack:
    #             res.append(stack[-1].val)
    #     return res


class BSTIterator:
    def push_leftmost_branch(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    """
    @param: root: The root of binary tree.
    """

    def __init__(self, root):
        self.stack = []
        self.push_leftmost_branch(root)

    """
    @return: True if there has next node, or false
    """

    def hasNext(self):
        return bool(self.stack)

    """
    @return: return next node
    """

    def _next2(self):
        node = self.stack.pop()
        if node.right:
            self.push_leftmost_branch(node.right)
        return node

    """ 32041
         [1]
         /
       [2]
       / \
      3   4
         /
        0
    2.next = 0
    4.next = 1     
    """  # 栈上保存的是从root到当前节点路径

    def _next(self):  # 这个模板 镜像修改后可以做prev访问
        node = self.stack[-1]  # 这就是这轮next的值 接下来准备下轮next的值到栈顶
        if node.right:  # 有右边节点 next = 右子树最小值  把右子树左侧入栈 待下轮next使用
            self.push_leftmost_branch(node.right)
        else:  # 无右边节点 next = 路径上第一个可以与 下一个节点构成左子树关系的节点  对如图上的1
            n = self.stack.pop()  # pop掉栈上所有右子树的部分 包括右子树根节点 栈顶为下轮next的值
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()
        return node

    def next(self):
        return self._next()


# class BSTIterator:
#     """ https://www.lintcode.com/problem/86/
#     @param: root: The root of binary tree.
#     """
#
#     @classmethod  # 将以root为根的子树的 最左边整条路径 入栈
#     def push_leftmost_branch(cls, root, stack):  # push leftmost branch of the subtree centered at root on to the stack
#         while root:
#             stack.append(root)
#             root = root.left
#
#     def __init__(self, root):
#         self.stack = []
#         BSTIterator.push_leftmost_branch(root, stack=self.stack)
#
#     @classmethod
#     def get_next(cls, stack):  # 精简版next stack上只保存还没有访问过的点
#         node = stack.pop()
#         if node.right:
#             BSTIterator.push_leftmost_branch(node.right, stack)  # 把右边节点为根 leftmost branch入栈
#         return node
#
#     @classmethod
#     def get_next1(cls, stack):  # 复杂版本next(镜像改下可以做prev遍历 inorder predecessor) invariant stack上始终保持 root到当前node路径
#         # get next node from given stack  using above algorithm
#         node = stack[-1]
#         if node.right:
#             BSTIterator.push_leftmost_branch(node.right, stack)
#         else:
#             n = stack.pop()  # 先让n = node
#             while stack and stack[-1].right == n:
#                 n = stack.pop()  # 退出循环时 stack[-1].right != n  那么只能stack[-1].left == n n为刚pop的节点
#         return node
#
#     def hasNext(self):
#         return bool(self.stack)
#
#     def next(self):
#         return self._next()
#
#     def _next(self):
#         # write your code here
#         return BSTIterator.get_next(self.stack)
