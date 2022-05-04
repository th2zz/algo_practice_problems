class Solution:
    # https://leetcode.cn/problems/find-peak-element/
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < nums[mid + 1]:
                start = mid
            elif nums[mid] > nums[mid + 1]:
                end = mid
        # no platau exists
        return start if nums[start] >= nums[end] else end
    
class Solution2:
    """
    https://www.lintcode.com/problem/75/?_from=ladder&fromId=161
    Description
There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peak if:

A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.

It's guaranteed the array has at least one peak.
The array may contain multiple peeks, find any of them.
The array has at least 3 numbers in it.
Example
Example 1:

Input:

A = [1, 2, 1, 3, 4, 5, 7, 6]
Output:

1
Explanation:

Returns the index of any peak element. 6 is also correct.
Example 2:

Input:

A = [1,2,3,4,1]
Output:

3
Explanation:

return the index of peek.

Challenge
Time complexity O(logN)O(logN)

Tags
Binary Search
Related Problems
1476
Peak Index in a Mountain Array
Easy
585
Maximum Number in Mountain Sequence
Medium
390
Find Peak Element II
Hard
不存在plateau
局部有序数组中 二分法解决ooxx问题 切一刀 判断在上升/下降区间 并向peak逼近
返回任意peak 索引
    A[0] < A[1] && A[A.length - 2] > A[A.length - 1]. 两边向中间升
    It's guaranteed the array has at least one peak.
    The array may contain multiple peeks, find any of them.
    The array has at least 3 numbers in it.

    @param A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):
        # peak不能在两端 所以在[1, len(A) - 2]查找
        start, end = 1, len(A) - 2
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < A[mid - 1]:  # 如果mid在下降区间 搜索左半边   也可以A[mid] > A[mid + 1]
                end = mid
            elif A[mid] < A[mid + 1]:  # 如果mid在上升区间 搜索右半边
                start = mid
            else:  # 否则mid为peak 不存在平原情况 平原情况无法2分 退化为O(n)
                return mid
        # 因为保证一定有peak, 返回start end中较大的那个
        return end if A[start] < A[end] else start
