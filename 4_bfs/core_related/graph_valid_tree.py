import collections
from typing import List


class Solution:
    """https://www.lintcode.com/problem/178/?_from=collection&fromId=161
        Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
        write a function to check whether these edges make up a valid tree.

    You can assume that no duplicate edges will appear in edges. Since all edges are undirected,
    [0, 1] is the same as [1, 0] and thus will not appear together in edges.

    Example
    Example 1:
    Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    Output: true.
    Example 2:

    Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    Output: false.
    TAG: bfs union find
    只是 len(edges)==n-1 不足以判定是否为联通
    例如 以下反例 len(edges) == len(nodes)
     [[0,1],[5,6],[6,7],[9,0],[3,7],[4,8],[1,8],[5,2],[5,3]]
    9-0-1-4-8
        |   |
        ----
    2-5-6-7-3
     |      |
     -------
        @param n: An integer
        @param edges: a list of undirected edges
        @return: true if it's a valid tree, or false
    """

    def validTree(
        self, n: int, edges: List[List[int]]
    ) -> bool:  # 树需要满足两个条件 连通的 没有环 所以bfs可以解决
        if n == 1 and len(edges) == 0:  # handle base case
            return True
        if len(edges) != n - 1:  # 排除不连通 和有环的情况 边的数量<n-1不连通 >n-1有环
            return False
        graph = collections.defaultdict(set)
        for u, v in edges:  # build undirected graph by two-way edges
            graph[u].add(v)
            graph[v].add(u)
        q = collections.deque([0])  # bfs检查是否为连通的
        visited = {0}
        print(graph)
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return len(visited) == n


#
#
# res = Solution().valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3]])
# print(res)
# 输入
# n =
# 5
# edges =
# [[0,1],[0,2],[0,3],[1,4]]
# 标准输出
# defaultdict(<class 'set'>, {0: {1, 2, 3}, 1: {0, 4}, 2: {0}, 3: {0}, 4: {1}})
# 输出
# true
# 预期结果
# true

# 输入
# n =
# 5
# edges =
# [[0,1],[1,2],[2,3],[1,3],[1,4]]
# 输出
# false
# 预期结果
# false
