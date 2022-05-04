"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """https://www.lintcode.com/problem/531/?fromId=161&_from=collection
    Algorithms
Medium
Accepted Rate
47%

DescriptionSolutionNotesDiscussLeaderboard
Description
Six degrees of separation is a philosophical problem, which means that everyone
 and everything can be connected through six steps or less.

Now give you a friendship, calculate how many steps two people can be connected
 through, if not, return -1.

Example
Example1

Input: {1,2,3#2,1,4#3,1,4#4,2,3} and s = 1, t = 4
Output: 2
Explanation:
    1------2-----4
     \          /
      \        /
       \--3--/
Example2

Input: {1#2,4#3,4#4,2,3} and s = 1, t = 4
Output: -1
Explanation:
    1      2-----4
                 /
               /
              3
Tags
Breadth First Search/BFS
Company
Microsoft
Related Problems
137
Clone Graph
Medium
    """
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):
        # write your code here
        pass
