class Solution:
    """https://www.lintcode.com/problem/443/?_from=collection&fromId=161
    Description
Given an array of integers, find how many pairs in the array such that their sum is bigger than a specific target number. Please return the number of pairs.

Example
Example 1:

Input: [2, 7, 11, 15], target = 24
Output: 1
Explanation: 11 + 15 is the only pair.
Example 2:

Input: [1, 1, 1, 1], target = 1
Output: 6
Challenge
Do it in O(1) extra space and O(nlogn) time.

Tags
Opposite Direction Two Pointers
Two Pointers
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """

    def twoSum2(self, nums: list, target):
        if not nums:
            return 0
        nums.sort()  # TODO remember to sort
        left, right = 0, len(nums) - 1
        res = 0
        while left < right:
            sum = nums[left] + nums[right]
            if sum <= target:
                left += 1
            else:
                res += right - left  # 从left开始到right -1 都是 sum > target
                right -= 1
        return res
