from typing import List


class Solution:  # https://leetcode.cn/problems/merge-intervals/
    """
        merge all overlapping intervals

    Example 1:

    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
    Example 2:

    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.

    Constraints:

    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])  # sort by start
        res = []
        # 这里[1,2] [2,3] 也会被认为是重合的  需要被合并
        for interval in sorted_intervals:
            # res empty or res[-1].end < interval.start = 无重合
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(
                    res[-1][1], interval[1]
                )  # update tail interval end value := max  if overlapped

        return res
