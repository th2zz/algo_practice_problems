class Solution:
    """
    https://www.lintcode.com/problem/447/?_from=ladder&fromId=161
    Given a big sorted array with non-negative integers sorted by non-decreasing order. The array is so big so that you
    can not get the length of the whole array directly,
    and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).

Find the first index of a target number. Your algorithm should be in O(log k),
where k is the first index of the target number.
Return -1, if the number doesn't exist in the array.
If you accessed an inaccessible index (outside of the array), ArrayReader.get will return 2,147,483,647.

Example
Example 1:

Input: [1, 3, 6, 9, 21, ...], target = 3
Output: 1
Example 2:

Input: [1, 3, 6, 9, 21, ...], target = 4
Output: -1
Challenge
O(logn) time, n is the first index of the given target number.
给一个大的排序数组，数组长度不可获取, 给一个reader 只能通过get(index)方式获取数组中元素 logn找到first pos of target
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # 本题题眼在于先用倍增法logK找到target会存在的范围 然后做二分 find first pos of target
        range_total = 1
        while reader.get(range_total - 1) < target:
            range_total = range_total * 2
        # 接下来是常规二分logK find first pos of target
        start, end = 0, range_total - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # target在右边
            if reader.get(mid) >= target:
                end = mid
            else:
                start = mid
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1