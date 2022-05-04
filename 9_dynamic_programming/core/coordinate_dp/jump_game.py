class Solution:  # https://leetcode.cn/problems/jump-game/
    """
    You are given an integer array nums. You are initially positioned at the array's first index,
    and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

给一个数组nums, nums[i]为位置i可跳步数 求能否reach last index
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0,
which makes it impossible to reach the last index.

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
    """

    def canJump(self, nums):
        max_i = 0  # init the furthest position that can be reached
        for i, jump in enumerate(nums):
            if max_i >= i and i + jump > max_i:  # if cur pos reachable, update furthest pos based on i
                max_i = i + jump  # 当前位置可达max_i >= i 则打擂台更新max_i
        return max_i >= len(nums) - 1


print(Solution().canJump([3, 2, 1, 0, 4]))
