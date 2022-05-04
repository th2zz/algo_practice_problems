from typing import List
"""
house robber, same set up but with circular array

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""


class Solution:  # https://leetcode.cn/problems/house-robber-ii/
    def rob_naive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # dp[i] amount of money we can rob at house i, so far
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[len(nums) - 1]

    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])
        # cannot rob the first and the last house at the same time, return max sol ([0..n-2], [1..n-1])
        else:
            return max(self.rob_naive(nums[0: length - 1]), self.rob_naive(nums[1: length]))

    def rob2(self, nums: List[int]) -> int:
        def robRange(start: int, end: int) -> int:  # rolling variable version
            first = nums[start]
            second = max(nums[start], nums[start + 1])
            for i in range(start + 2, end + 1):
                first, second = second, max(first + nums[i], second)
            return second

        length = len(nums)
        if length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])
        else:  # can either rob the first house or the last house
            return max(robRange(0, length - 2), robRange(1, length - 1))
