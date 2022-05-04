import heapq
from typing import (
    List,
)


class Solution:
    """https://www.lintcode.com/problem/544/?_from=collection&fromId=161
    Medium
    Given an integer array, find the top k largest numbers in it.

Example
Example1

Input: [3, 10, 1000, -99, 4, 100] and k = 3
Output: [1000, 100, 10]
Example2

Input: [8, 7, 6, 5, 4, 3, 2, 1] and k = 5
Output: [8, 7, 6, 5, 4]
Tags
Heap
Related Problems
613
High Five
Medium
550
Top K Frequent Words II
Hard
545
Top k Largest Numbers II
Medium
471
Top K Frequent Words
Medium
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """

    # def topk(self, nums: List[int], k: int) -> List[int]:  # 动态top k largest: min heap
    #     q = []
    #     for n in nums:
    #         heapq.heappush(q, n)  # minheap
    #         if len(q) > k:
    #             heapq.heappop(q)
    #     res = []
    #     while q:  # return res in decreasing order
    #         res.insert(0, heapq.heappop(q))
    #     return res

    def partition(self, nums, start, end):
        l, r = start, end
        pivot = nums[(l + r) // 2]  # pivot index
        while l <= r:
            while l <= r and nums[l] < pivot:
                l += 1
            while l <= r and nums[r] > pivot:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        return l, r

    def quick_select(self, k, nums, start, end):  # find element at index k
        if start == end:
            return nums[start]
        l, r = self.partition(nums, start, end)
        if k <= r:
            return self.quick_select(k, nums, start, r)
        if k >= l:
            return self.quick_select(k, nums, l, end)  # TODO 还是找第k大的数 因为k始终是一个相对所有数的 绝对的rank 不是找局部的第k大 返回值只在最上层使用
        return nums[k]  # r<k<l r, l中间相隔一个

    def topk(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []
        self.quick_select(len(nums) - k, nums, 0, len(nums) - 1)  # O(n)完成partition
        # nums[len(nums) - k:] 为top k largest
        return sorted(nums[len(nums) - k:], reverse=True)
