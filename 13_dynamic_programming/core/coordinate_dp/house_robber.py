"""
输入: 一个int array 代表 系列房子 每个房子内有一定金额的钱 (非负), 不可以抢劫相邻的房子 问可以抢到的最大金额
Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

dp[0] = nums[0]
dp[1] = max(nums[0], nums[1])
dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
"""


class Solution:  # https://leetcode.cn/problems/house-robber/
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)  # dp[i] amount of money we can rob at house i, so far
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[len(nums) - 1]
