# An Iterative Python program to do dfs traversal from
# a given source vertex. dfs(int s) traverses vertices
# reachable from s.

# This class represents a directed graph using adjacency
# list representation
from collections import deque


class Graph:
    def __init__(self, V):  # Constructor
        self.V = V  # No. of vertices
        self.adj = [[] for _ in range(V)]  # adjacency lists

    def add_edge(self, v, w):  # to add an edge to graph
        self.adj[v].append(w)  # Add w to v’s list.

    # def dfs(self, s):  # 有环 or 无环
    #     stack = deque([s])
    #     visited = set()  # 这种写法可以解决有环的图 因为访问过的一定不会再重新访问
    #     while stack:
    #         node = stack.pop()
    #         if node not in visited:  # 这种写法可以解决有环的图 因为访问过的一定不会再重新访问 但节点可能重复进入队列 会指数级上升
    #             print(node, end=' ')
    #             visited.add(node)  # 或者可以说叫 expanded 已经处理过
    #             for next_node in self.adj[node]:
    #                 if next_node not in visited:
    #                     stack.append(next_node)
    #
    # def bfs(self, s):  # 有环 or 无环
    #     q = deque([s])
    #     visited = set()  # 这种写法可以解决有环的图 因为访问过的一定不会再重新访问
    #     while q:
    #         node = q.popleft()
    #         if node not in visited:  # 这种写法可以解决有环的图 因为访问过的一定不会再重新访问  但节点可能重复进入队列 会指数级上升
    #             print(node, end=' ')
    #             visited.add(node)  # 或者可以说叫 expanded 已经处理过
    #             for next_node in self.adj[node]:
    #                 if next_node not in visited:
    #                     q.append(next_node)
    def bfs(self, s):  # 这种只能作用于无环图 入队和标记visited时同步的
        q = deque([s])
        visited = {s}  # BFS直接 入队时同步加到visited
        while q:
            node = q.popleft()
            print(node, end=' ')
            for next_node in self.adj[node]:
                if next_node not in visited:  # BFS直接 入队时同步加到visited
                    visited.add(node)
                    q.append(next_node)
    def dfs(self, s):  # 和BFS对称的写法 这种只能作用于无环图
        visited = {s}
        stack = deque([s])
        while stack:
            node = stack.pop()
            print(node, end=' ')
            for next_node in self.adj[node]:
                if next_node not in visited:
                    visited.add(node)
                    stack.append(next_node)


# Driver program to test methods of graph class

g = Graph(7)  # Total 5 vertices in graph
g.add_edge(1, 0)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 0)
# g.add_edge(2, 1)  # circle
# g.add_edge(1, 2)  # circle
g.add_edge(2, 5)
g.add_edge(5, 2)
g.add_edge(5, 6)
g.add_edge(6, 5)
g.add_edge(0, 3)
g.add_edge(3, 0)
g.add_edge(1, 4)
g.add_edge(4, 1)
#    -------
#    |     |
#  4-1-0---2---5--6
#      |
#      3
#

print("dfs")
g.dfs(0)  # 0325614
print()
print("bfs")
g.bfs(0)  # 0123456
