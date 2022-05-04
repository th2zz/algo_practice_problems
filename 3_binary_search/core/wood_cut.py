class Solution:
    """https://www.lintcode.com/problem/183/?_from=ladder&fromId=161
    Description
Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

The unit of length is centimeter.The length of the woods are all positive integers,you couldn't cut wood into float length.If you couldn't get >= k pieces, return 0.

Example
Example 1

Input:
L = [232, 124, 456]
k = 7
Output: 114
Explanation: We can cut it into 7 pieces if any piece is 114cm long, however we can't cut it into 7 pieces if any piece is 115cm long.
Example 2

Input:
L = [1, 2, 3]
k = 7
Output: 0
Explanation: It is obvious we can't make it.
Challenge
O(n log Len), where Len is the longest length of the wood.
给定一组木头长度数组(unsorted), k 至少要切的段数, 求切>=k段等长木头时最长wood cut
在映射关系(结果集) (wood cut长度)上进行二分 来间接的调整段数 段数逼近于k = maximize wood cut长度
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # 这里是二分木头长度 并根据可切分段数调整木头长度, (段数和长度负相关) 使段数逼近于k = maximize wood cut长度
        if not L:
            return 0
        # 木头长度下界为1 上界为 min(L中最长木头, 总长度和切分均值(无限制下切成k段最长这么长))
        # 这里只是取个两个最大值 中的最小值做lowerbound上限
        start, end = 1, min(max(L), sum(L) // k)
        if end < 1:  # TODO 如果end小于1不可能完成任务 返回0
            return 0
        while start + 1 < end:
            mid = (start + end) // 2
            # 长度为mid的木头切分总数 >= 目标段总数 继续增长木头长度 (减少段数) 让段数逼近k
            if self.get_count(L, mid) >= k:
                start = mid
            # 长度为mid的木头总数 < 目标总段数 继续缩短木头长度 (增加段数) 让段数逼近k
            else:
                end = mid
        # 因为之前排除了无解的情况 所以这里一定有解 非start即end
        # 如果end符合要求 首选end 因为end更长 否则选start
        return end if self.get_count(L, end) >= k else start

    def get_count(self, cut_len, l):
        return sum(piece_len // cut_len for piece_len in l)
