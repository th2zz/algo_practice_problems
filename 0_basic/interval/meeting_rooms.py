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
    def minMeetingRooms(self, intervals: List[List[int]]):
        intervals.sort(key=lambda x:x[0])  # TODO sort by start time
        earliest_endtimes: list[int] = [intervals[0][1]]  # init heap with first item; earliest endtime so far
        res = 1  # start from 1 (first meeting)
        for i in range(1, len(intervals)):  # traverse remaining intervals; heap[0] = peeek!
            interval = intervals[i]
            if interval[0] < earliest_endtimes[0]: # conflict 会议开始时间 < 最早结束时间，需增加会议室
                res += 1
            else: # no conflict 可以在最早结束的会议之后开始当前会议，end this meeting
                heapq.heappop(earliest_endtimes)   # pop from heap 
            heapq.heappush(earliest_endtimes, interval[1])  # add curr interval end time to heap
        return res
