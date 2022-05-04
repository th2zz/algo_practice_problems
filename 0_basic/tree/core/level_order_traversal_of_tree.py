""" https://www.lintcode.com/problem/1533/
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import collections


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):  # 掌握常规写法即可 分层bfs
        if not root:
            return []
        results = []
        queue = collections.deque([root])  # 循环过程中 queue始终保持着只含同一层的东西
        while queue:
            level = []  # 核心 每轮都是处理完当前队列里东西/expand完为止 这些处理的东西都是来自同一层
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(level)
        return results

    def levelOrder_1q(self, root):
        if not root:
            return []
        queue = collections.deque([root])
        results = []
        while queue:
            results.append([node.val for node in queue])
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return results

    def levelOrder_2q(self, root):
        if not root:
            return []
        queue = [root]
        results = []
        while queue:
            # expand fringe using next queue; switch queue to next queue
            next_queue = []
            results.append(node.val for node in queue)
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        return results

    def levelOrder_dummy(self, root):
        if not root:
            return []
        queue = collections.deque([root, None])
        results, level = [], []
        while queue:
            node = queue.popleft()
            if node is None:
                results.append(level)
                level = []
                if queue:
                    queue.append(None)
                continue
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return results
