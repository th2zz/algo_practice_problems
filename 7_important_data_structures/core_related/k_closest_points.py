from typing import (
    List,
)
from lintcode import (
    Point,
)
import math
import heapq

"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""


class Solution:
    """https://www.lintcode.com/problem/612/?_from=collection&fromId=161
    medium
    Given some points and an origin in two-dimensional space,
    Find k points from points which are closest to origin.
    Return to the answer from small to large according to Euclidean distance.
    If two points have the same Euclidean distance, they are sorted by x values.
    If the x value is the same, then we sort it by the y value.

Example 1:

Input: points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
Output: [[1,1],[2,5],[4,4]]
Example 2:

Input: points = [[0,0],[0,9]], origin = [3, 1], k = 1
Output: [[0,0]]

Challenge
O(nlogn) is OK, but can you think of a solution to O(nlogk)？

Tags
Heap Mathmatics
Company
LinkedIn Amazon Microsoft
Related Problems
460 Find K Closest Elements Medium
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """

    def get_distance(self, source, point):
        return math.sqrt(pow((point.x - source.x), 2) + pow((point.y - source.y), 2))

    def k_closest1(self, points: List[Point], origin: Point, k: int) -> List[Point]:
        if k > len(points):  # not enough for k
            return []
        q = [(self.get_distance(origin, p), p.x, p.y, p) for p in points]
        heapq.heapify(q)
        res = []
        for _ in range(k):  # O(klogn)  heapify O(n) k次heappop
            _, _, _, p = heapq.heappop(q)
            res.append(p)
        return res

    # 在线top k smallest算法 使用fixed size k maxheap
    def k_closest(self, points: List[Point], origin: Point, k: int) -> List[Point]:
        if k > len(points):
            return []
        q = []  # fixed size k heap
        for p in points:  # O(nlogk)
            heapq.heappush(q, (-self.get_distance(origin, p), -p.x, -p.y, p))  # push to maxheap
            if len(q) > k:  # 超过容量 去掉最大的  最后堆里剩的是前k个最小的
                heapq.heappop(q)
        res = []
        while q:
            _, _, _, p = heapq.heappop(q)  # 按题目要求排序结果
            res.insert(0, p)
        return res
