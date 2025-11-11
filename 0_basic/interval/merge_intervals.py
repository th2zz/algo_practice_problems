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
    
    重合的定义 两个区间重合的充分且必要条件是 A.start <= B.end and B.start <= A.end
    两个区间不重合的充分且必要条件是 A.end < B.start or B.end < A.start
    无重合的判断： 末尾的end < 下一个区间的start
    else 就是重合的情况  需要合并
    将末尾区间认为是A, 下一个区间认为是B
    A.end >= B.start已经在else中成立
    A.start <= B.end 也是成立的 因为A.start <= B.start (已经排序过了) <= B.end (题目限定了start <= end)
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        for interval in sorted_intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(
                    res[-1][1], interval[1]
                )  # update tail interval end value := max  if overlapped to merge
        return res
