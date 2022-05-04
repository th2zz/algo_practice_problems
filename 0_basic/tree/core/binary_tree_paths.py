""" https://www.lintcode.com/problem/480/
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root node of the binary tree
    @return:
        list: all root-to-leaf paths  给定一个二叉树root 找到所有root to leaf path
    """

    def binary_tree_paths(self, root):  # DIVIDE AND CONQUER
        # write your code here
        paths = []
        if not root:
            return paths
        if not root.left and not root.right:  # 整棵树的paths = 左半边树paths + 右半边树paths
            return [str(root.val)]
        for path in self.binary_tree_paths(root.left):
            paths.append(str(root.val) + "->" + path)
        for path in self.binary_tree_paths(root.right):
            paths.append(str(root.val) + "->" + path)
        return paths

    def binaryTreePaths2(self, root):
        if not root:
            return []
        paths = []
        self.find_paths(root, [root], paths)
        return paths

    def find_paths(self, node, path, paths):  # find all paths by backtracking (DFS)
        if not node:
            return
        if not node.left and not node.right:
            paths.append('->'.join([str(n.val) for n in path]))
            return
        path.append(node.left)
        self.find_paths(node.left, path, paths)  # solve left half subproblem
        path.pop()  # backtrack for variable path 此时path状态多了个node.left 需要还原回去 解决右半边
        path.append(node.right)
        self.find_paths(node.right, path, paths)  # solve right half subproblem
        path.pop()  # 左右两边找完了就是找完了 不需要关心节点本身 TODO 节点本身在主函数调递归参数path起始值里
