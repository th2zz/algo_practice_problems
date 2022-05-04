import enum
from typing import List


class Solution:  # https://leetcode.cn/problems/insert-interval/
    """https://mp.weixin.qq.com/s/ioUlNa4ZToCrun3qb4y4Ow
    Insert newInterval into intervals such that

    1. intervals is still sorted in ascending order by starti

    2. intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

    Return intervals after the insertion.

    Example 1:

    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]
    Example 2:

    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

    Constraints:

    0 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 105
    intervals is sorted by starti in ascending order.
    newInterval.length == 2
    0 <= start <= end <= 105
    """

    # 1. append all non-overlapping intervals until there is an overlap
    #    now interval.end >= newInterval.start  e.g. [2,4] [3,5] or [2,4] [4,5]
    # 2. construct a big interval by merging consecutive overlapping intervals and append once we are done
    #    绿区间为我们在遍历的区间，蓝区间为新插入区间 想象蓝区间从一众绿区间上划到右边
    #    如果有重叠，则必须满足 绿区间的左端 <= 蓝区间的右端  绿左<=蓝右
    #    为什么不能判断 绿右>= 蓝左 ? [蓝]  [绿] 因为如果绿在蓝后面 也满足绿右>=蓝左
    # 3. now no overlapping intervals anymore, append rest of intervals remained
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res
