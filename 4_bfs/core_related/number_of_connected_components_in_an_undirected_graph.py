import collections


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = set()


class Solution:  # https://leetcode.cn/problems/number-of-connected-components-in-an-undirected-graph/
    # n个节点 edges[i] = [[a, b]] ~ edge a<->b.
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)
        visited = set()
        # res = 0  # connected comp cnt
        res = []  # actual connected component, list[list[int]]
        for i in range(
            n
        ):  # must traverse range of n, instead of only looking at graph.keys. because there can be isolated points
            if i not in visited:
                self.bfs(i, res, visited=visited, graph=graph)
                # res += 1
        # return res
        return len(res)

    def bfs(self, start_node, res, visited, graph):
        q = collections.deque([start_node])
        visited.add(start_node)
        nodes_label_traversed = []  # 所有遍历到的label
        while q:
            node = q.popleft()
            nodes_label_traversed.append(node)  # 题目要求返回label
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        # nodes_label_traversed.sort()  # 题目要求 每个连通分量里节点按label排序
        res.append(nodes_label_traversed)
