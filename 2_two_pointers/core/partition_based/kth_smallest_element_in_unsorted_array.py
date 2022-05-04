class Solution:
    """https://www.lintcode.com/problem/461/?_from=collection&fromId=161
    Description
Find the kth smallest number in an unsorted integer array.

Example
Example 1:

Input: [3, 4, 1, 2, 5], k = 3
Output: 3
Example 2:

Input: [1, 1, 1], k = 2
Output: 1
Challenge
An O(nlogn) algorithm is acceptable, if you can do it in O(n), that would be great.

Tags
Quick Select
Sort
Related Problems
5
Kth Largest Element
Medium
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """

    def kth_smallest(self, k: int, nums):
        if not nums:
            return 0
        return self.quick_select(nums, 0, len(nums) - 1, k - 1)

    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[k]
        left, right = self.partition(nums, start, end)  # TODO 注意这里pivot取值 为自动取中点做pivot
        if k >= left:
            return self.quick_select(nums, left, end, k)  # TODO 注意return
        if k <= right:
            return self.quick_select(nums, start, right, k)
        return nums[k]

    def partition(self, nums, start, end):
        pivot = nums[(start + end) // 2]
        while start <= end:
            while start <= end and nums[start] < pivot:
                start += 1
            while start <= end and nums[end] > pivot:
                end -= 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return start, end
