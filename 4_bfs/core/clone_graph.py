import collections


class Solution:
    """Description https://leetcode.cn/problems/clone-graph/
    Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
    Nodes are labeled uniquely.

    You need to return a deep copied graph, which has the same structure as the original graph,
    and any changes to the new graph will not have any effect on the original graph.

    # Definition for a Node.
    class Node:
        def __init__(self, val = 0, neighbors = None):
            self.val = val
            self.neighbors = neighbors if neighbors is not None else []

    @param node: A undirected graph node
    @return: deep copy of this undirected graph node, the node with the same label as the input node.
    """

    def cloneGraph(self, node):
        if not node:
            return None
        nodes: list = self.find_all_nodes_by_bfs(node)
        old2new: dict = self.copy_nodes(nodes)
        self.copy_edges(nodes, old2new)
        return old2new[node]

    def find_all_nodes_by_bfs(self, node):
        q = collections.deque([node])
        visited = {node}  # TODO visited初始化加上node
        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return list(visited)

    def copy_edges(self, nodes: list, old2new: dict):
        for n in nodes:
            for neighbor in n.neighbors:
                old2new[n].neighbors.append(
                    old2new[neighbor]
                )  # 旧节点neighbors同步到新节点

    def copy_nodes(self, nodes: list):
        return {n: Node(n.val) for n in nodes}  # 创建 {旧节点:新节点,...} mapping
