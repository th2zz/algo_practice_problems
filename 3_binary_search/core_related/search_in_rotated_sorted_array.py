
class Solution:  # https://leetcode.cn/problems/search-in-rotated-sorted-array/
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start,end = 0, n - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < nums[n - 1]:  # on smaller part
                if nums[mid] <= target <= nums[n - 1]:
                    start = mid
                else:
                    end = mid
            elif nums[mid] > nums[0]:  # on larger part
                if nums[0] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

class Solution2:
    """https://www.lintcode.com/problem/62/?_from=collection&fromId=161
    Description
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Example
Example 1:

Input:

array = [4, 5, 1, 2, 3]
target = 1
Output:

2
Explanation:

1 is indexed at 2 in the array.

Example 2:

Input:

array = [4, 5, 1, 2, 3]
target = 0
Output:

-1
Explanation:

0 is not in the array. Returns -1.

Challenge
O(logN) time
hire = 2 pass bs, strong hire = 1 pass bs
ASSUME left rotate
2pass binary search: first find minimum in rotated sorted array then we know which half we are on, then do a binary search again
1pass binary search:
    after picking mid,
        By comparing with last or first element, first determine where mid is located:
        either left larger half or right smaller half
        after determine where the cut is, [start...mid(cut)...end]  eliminate half search space depends on where target is
    在一个有序 无重复旋转数组中搜索目标值
    中点切一刀 通过和起始位置/终点位置元素比较 确定在大半边还是左半边
        然后确定target位置 小半边的话 target可以在 [mid...end] 直接移动start=>mid 不在则移动end=>mid
        大半边同理
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """

    def search(self, A, target):
        if not A:
            return -1
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < A[len(A) - 1]:  # cut is on smaller half
                if A[mid] <= target <= A[end]:  # on right half [mid, end]
                    start = mid
                else:  # reduce to original problem again
                    end = mid
            else:  # cut is on larger half
                if A[start] <= target <= A[mid]:  # on left half [start, mid]  # TODO 这里必须严格这样写
                    end = mid
                else:
                    start = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
