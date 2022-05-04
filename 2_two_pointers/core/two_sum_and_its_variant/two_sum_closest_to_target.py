import sys
from typing import (
    List,
)


class Solution:
    """https://www.lintcode.com/problem/533/?_from=collection&fromId=161
    Description
Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.

Return the absolute value of difference between the sum of the two numbers and the target.

Example
Example1

Input:  nums = [-1, 2, 1, -4] and target = 4
Output: 1
Explanation:
The minimum difference is 1. (4 - (2 + 1) = 1).
Example2

Input:  nums = [-1, -1, -1, -4] and target = 4
Output: 6
Explanation:
The minimum difference is 6. (4 - (- 1 - 1) = 6).
Challenge
Do it in O(nlogn) time complexity.
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """

    def two_sum_closest(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        left, right, res = 0, len(nums) - 1, sys.maxsize
        while left < right:
            sum = nums[left] + nums[right]
            absval = abs(sum - target)
            if sum < target:
                left += 1
            else:  # 在two sum过程中记录最小difference  =target怎么处理无所谓
                right -= 1
            res = min(res, absval)
        return res
