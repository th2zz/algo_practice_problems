"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
import collections


class Solution:
    """https://www.lintcode.com/problem/618/?_from=collection&fromId=161
    Given a undirected graph, a node and a target, return the nearest node to given node which value of it is target, return NULL if you can't find.

There is a mapping store the nodes' values in the given parameters.

It's guaranteed there is only one available solution

Example
Example 1:

Input:
{1,2,3,4#2,1,3#3,1,2#4,1,5#5,4}
[3,4,5,50,50]
1
50
Output:
4
Explanation:
2------3  5
 \     |  |
  \    |  |
   \   |  |
    \  |  |
      1 --4
Give a node 1, target is 50

there a hash named values which is [3,4,10,50,50], represent:
Value of node 1 is 3
Value of node 2 is 4
Value of node 3 is 10
Value of node 4 is 50
Value of node 5 is 50

Return node 4
Example 2:

Input:
{1,2#2,1}
[0,1]
1
1
Output:
2
Tags
Breadth First Search/BFS
Company
Apple
Related Problems
814
Shortest Path in Undirected Graph
Medium
611
Knight Shortest Path
Medium
70
Binary Tree Level Order Traversal II
Medium
BFS CAN ALWAYS solve the single source shortest path problem
IF the weight of each edge between any two vertices in the graph is the same.
This is because BFS will find all paths that are 1 edge away from the source,
followed by all paths that are two edges away from the source, and so on.
If the edges are all length x=1 (or the same length), then BFS will find all paths of length 1x from the source,
followed by all paths of length 2x, followed by all paths of length 3x, and so on.
This will allow BFS to find the shortest path from the source node to any predetermined sink node.

What happens though if the edge weights are not the same? Then BFS fails to work.
This is because BFS terminates when it first finds the sink node in its search of the graph.

给定一张 无向图，一个 节点 以及一个 目标值，返回距离这个节点距离最近 且 值为目标值的节点，如果不能找到则返回 NULL。
在给出的参数中, 我们用 hashmap values 来存节点的值
保证答案唯一
朴素bfs找到值为target的节点 (找到的target点自动为最短距离点 因为bfs可以被用来解决简单图最短路径)
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """

    def searchNode(self, graph, values, node, target):
        q = collections.deque([node])
        visited = {node}
        while q:
            n = q.popleft()
            if values[n] == target:
                return n
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return None
