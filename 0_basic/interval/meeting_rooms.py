from typing import List
import heapq

class Solution:
    # 判断区间是否无重叠  (判断能否参加所有会议)  从第一个开始 相邻的作比较 overlap=False otherwise True
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x : x[0])
        if not sorted_intervals:
            return True
        for i in range(1, len(sorted_intervals)):
            interval = sorted_intervals[i]
            prev_interval = sorted_intervals[i - 1]
            if prev_interval[1] > interval[0]:  # [1, 2] [2,3] not counted as overlap
                return False
        return True


    # return min# meeting rooms to accommodate all meetings  https://leetcode.cn/problems/meeting-rooms-ii/
    # 新来的meeting需要考虑当前所有active会议室的 最早结束时间 如果不能满足 则需要增加会议室
    # 会议与scheduleing不同的地方在于 必须优先处理开始时间最早的 先来先到的基础下找受限制的最优解, 而scheduling是全知全能的求最优解
    # sort by start time
    # then use min-heap to track earliest end time of active meetings and init with first meeting end time
    # traverse remaining meeting intervals from 2nd meeting
    #    if curr meeting start time < meeting with earliest end time in heap: conflict need new room
    #        increment room count
    #    else: no conflict can use this room, pop earliest end time from heap
    #    push curr meeting end time to heap
    # here to satisfy the check of conflict A.start < B.end and B.start < A.end
    # let the earliest end time meeting be A, current meeting be B
    # we are checking B.start < A.end, 
    # A.start < B.end is guaranteed to be true because A.start < B.start < B.end
    # A starts before B because of sorting by start time 
    # and we are processing meetings in that order during initialization of heap and traversal
    # an item that has already enqueued to heap must have started before current meeting
    # 一般情况下都需要按开始排序区间 只需要比较后面那个区间的开始时间和前面区间的结束时间 来判断是否overlap
    def minMeetingRooms(self, intervals: List[List[int]]):
        intervals.sort(key=lambda x:x[0])
        earliest_endtimes: list[int] = [intervals[0][1]]
        res = 1
        for i in range(1, len(intervals)):  # traverse remaining intervals; heap[0] = peeek!
            interval = intervals[i]
            if interval[0] < earliest_endtimes[0]: # conflict 会议开始时间 < 最早结束时间，需增加会议室
                res += 1
            else:
                heapq.heappop(earliest_endtimes) 
            heapq.heappush(earliest_endtimes, interval[1])
        return res
