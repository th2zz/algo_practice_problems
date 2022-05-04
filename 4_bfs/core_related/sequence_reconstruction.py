import collections
from typing import (
    List,
)


class Solution:
    """https://www.lintcode.com/problem/605/?_from=collection&fromId=161
    Medium
Accepted Rate
23%
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs.
The org sequence is a permutation of the integers from 1 to n, with 1≤n≤10^4.
Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e.,
 a shortest sequence so that all sequences in seqs are subsequences of it).
 Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Possible duplicate sequences in seqs

Example
Example 1:

Input:org = [1,2,3], seqs = [[1,2],[1,3]]
Output: false
Explanation:
[1,2,3] is not the only one sequence that can be reconstructed,
because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:

Input: org = [1,2,3], seqs = [[1,2]]
Output: false
Explanation:
The reconstructed sequence can only be [1,2], can't reconstruct the sequence [1,2,3].
Example 3:

Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
Output: true
Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Example 4:

Input:org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
Output:true
Tags
Topological Sort
Breadth First Search/BFS
Company
Google
Airbnb
Related Problems
815
Course Schedule IV
Hard
616
Course Schedule II
Medium
127
Topological Sorting
Medium
https://en.wikipedia.org/wiki/Shortest_common_supersequence_problem
a sequence U is a common supersequence of x, y if items can be removed from U to produce x and y
给定一个序列org，一堆序列seqs,
如果可以从 这堆序列中 构成 shortest common supersequence org, 那么org是seqs中所有序列的 shortest common
supersequence, seqs这些序列都是org的子序列, 我们叫这个操作为"reconstruction"
判断是否有且只有一个序列org 可以被reconstructed from seqs
人话:
求拓扑序是否唯一   判断标准是队列中是否始终有且只有1个元素
主要难点在于理解题意和构图
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequence_reconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        graph = self.build_graph(seqs)
        topo_order = self.topo_sort(graph)
        return topo_order == org

    def build_graph(self, seqs):  # adjacency list
        graph = {}
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()  # init, put all node as key
        for seq in seqs:  # 每一个seq都代表了一系列边的定义 将这些边还原到图里 e.g. [1,2] => 1->2
            for i in range(1, len(seq)):  # graph[from_node].add(to_node) from_node index: [0...len(seq)-2] to_node index: [1...len(seq)-1]
                graph[seq[i - 1]].add(seq[i])
        return graph

    def topo_sort(self, graph):
        indegrees = self.get_indegrees(graph)
        q = collections.deque([n for n in graph.keys() if indegrees[n] == 0])
        topo_order = []
        while q:
            if len(q) > 1:
                return None
            n = q.popleft()
            topo_order.append(n)
            for neighbor in graph[n]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)
        if len(topo_order) == len(graph):
            return topo_order
        return None

    def get_indegrees(self, graph):
        indegrees = {n: 0 for n in graph.keys()}
        for n in graph:
            for neighbor in graph[n]:
                indegrees[neighbor] += 1
        return indegrees
