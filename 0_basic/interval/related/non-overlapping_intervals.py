from heapq import merge
from typing import List


class Solution:  # https://leetcode.cn/problems/non-overlapping-intervals/
    """
    Given an array of intervals intervals
    return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
    """
    # 求最少删除多少区间 使得区间列表里区间不重合 / 为了完成尽量多的任务 需要drop最少多少任务
    # 他的对偶问题是个经典贪心scheduling问题  操作系统中 怎么样schedule任务 使得可以完成的任务数量最多
    # 求解对偶问题 然后求出原问题解
    # ans:= 选出最多数量的区间 使得他们互不重合 / the maximum number of non-overlapping intervals / 给一堆课表 去上课  最多可以上多少课(no conflict), sort by end time

    def maxNonOverlappingIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        earliest_endtime = intervals[0][1]
        ans = 1
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] >= earliest_endtime:  # no overlap
                ans += 1
                earliest_endtime = interval[1]
        return ans

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        return len(intervals) - self.maxNonOverlappingIntervals(intervals=intervals)
