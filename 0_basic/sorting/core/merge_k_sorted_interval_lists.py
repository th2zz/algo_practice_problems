"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """https://www.lintcode.com/problem/577/
本题和merge k sorted arrays一样区别是如何merge list of区间 总是把start小的push back到result尾部
实现push back: 空的 / (no overlap)不需要与尾部区间合并 直接append; 有overlap 与尾部区间合并  end换为较大end

Merge K sorted interval lists into one sorted interval list. You need to merge overlapping intervals too.

Example
Example1

Input: [
  [(1,3),(4,7),(6,8)],
  [(1,2),(9,10)]
]
Output: [(1,3),(4,8),(9,10)]
Example2

Input: [
  [(1,2),(5,6)],
  [(3,4),(7,8)]
]
Output: [(1,2),(3,4),(5,6),(7,8)]
Tags
Heap
Divide and Conquer
Company
Airbnb
Related Problems
839
Merge Two Sorted Interval Lists
Easy

    """
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """

    def mergeKSortedIntervalLists(self, intervals):
        return self.merge_helper(0, len(intervals) - 1, intervals)

    def push_back(self, interval, intervals):
        # 如何追加一个interval到intervals list: 空的/无重叠直接加 有重叠则与尾区间合并
        # no overlap or empty: directly append
        if not intervals or interval.start > intervals[-1].end:
            intervals.append(interval)
        # overlap set last interval's end to be larger end
        intervals[-1].end = max(intervals[-1].end, interval.end)

    def merge2_intervals_list(self, l1, l2):
        p1, p2 = 0, 0  # 本题和merge arrays一样区别是如何merge list of区间 总是把start小的追到list尾部
        res = []
        while p1 < len(l1) and p2 < len(l2):
            if l1[p1].start < l2[p2].start:
                self.push_back(l1[p1], res)
                p1 += 1
            else:
                self.push_back(l2[p2], res)
                p2 += 1
        while p1 < len(l1):
            self.push_back(l1[p1], res)
            p1 += 1
        while p2 < len(l2):
            self.push_back(l2[p2], res)
            p2 += 1
        return res

    def merge_helper(self, start, end, intervals):
        if start == end:  # base case 1 list of intervals, directly return no merge needed
            return intervals[start]
        mid = (start + end) // 2
        left = self.merge_helper(start, mid, intervals)
        right = self.merge_helper(mid + 1, end, intervals)
        return self.merge2_intervals_list(left, right)
