"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""



class Solution:
    """https://www.lintcode.com/problem/839/
    Description
Merge two sorted (ascending) lists of interval and return it as a new sorted list.
The new sorted list should be made by splicing together the intervals of the two lists and sorted in ascending order.

The intervals in the given list do not overlap.
The intervals in different lists may overlap.
Example
Example1

Input: list1 = [(1,2),(3,4)] and list2 = [(2,3),(5,6)]
Output: [(1,4),(5,6)]
Explanation:
(1,2),(2,3),(3,4) --> (1,4)
(5,6) --> (5,6)
Example2

Input: list1 = [(1,2),(3,4)] and list2 = [(4,5),(6,7)]
Output: [(1,2),(3,5),(6,7)]
Explanation:
(1,2) --> (1,2)
(3,4),(4,5) --> (3,5)
(6,7) --> (6,7)
Tags
Same Direction Two Pointers
Greedy
Two Pointers
Sort
Company
Uber
Related Problems
577
Merge K Sorted Interval Lists
Medium
486
Merge K Sorted Arrays
Medium
156
Merge Intervals
Easy
165
Merge Two Sorted Lists
Easy
104
Merge K Sorted Lists
Medium
64
Merge Sorted Array (easy version)
Easy
6
Merge Two Sorted Arrays
Easy

    """
    """
    @param list1: a list of intervals
    @param list2: another list
    @return: the new sorted list of interval; overlapped intervals from different list are merged
    """

    def push_back(self, intervals, interval):
        if not intervals:  # empty append
            intervals.append(interval)
            return
        if intervals[-1].end < interval.start:  # no overlap merge safely by append
            intervals.append(interval)
            return
        intervals[-1].end = max(intervals[-1].end, interval.end)  # have overlap, choose larger end

    def mergeTwoInterval(self, list1, list2):
        # overlap = merge needed
        i, j, n, m = 0, 0, len(list1) - 1, len(list2) - 1
        res = []
        while i <= n and j <= m:
            if list1[i].start < list2[j].start:
                self.push_back(res, list1[i])
                i += 1
            else:
                self.push_back(res, list2[j])
                j += 1
        while i <= n:
            self.push_back(res, list1[i])
            i += 1
        while j <= m:
            self.push_back(res, list2[j])
            j += 1
        return res

# list1 = [Interval(1, 2), Interval(3, 4)]
# list2 = [Interval(4, 5), Interval(6, 7)]
# #  [(1,2),(3,5),(6,7)]
# res = Solution().mergeTwoInterval(list1, list2)
# for item in res:
#     print(f"{(item.start, item.end)} ")
# Input: list1 = [(1,2),(3,4)] and list2 = [(2,3),(5,6)]
# Output: [(1,4),(5,6)]
# list1 = [Interval(1, 2), Interval(3, 4)]
# list2 = [Interval(2, 3), Interval(5, 6)]
# res = Solution().mergeTwoInterval(list1, list2)
# for item in res:
#     print(f"{(item.start, item.end)} ")