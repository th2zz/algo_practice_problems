class Solution:
    """https://www.lintcode.com/problem/608/?_from=collection&fromId=161
    Description
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Example
Example 1:

Input: nums = [2, 7, 11, 15], target = 9
Output: [1, 2]
Example 2:

Input: nums = [2,3], target = 5
Output: [1, 2]
Tags
Hash Table
Opposite Direction Two Pointers
Two Pointers
Company
Amazon
2sum 输入数组有序 则最优解为相向双指针
输入数组无序 最优解为hashmap
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        table = {}
        for i, n in enumerate(nums):
            counter_part = target - n
            if counter_part in table:
                return [table[counter_part] + 1, i + 1]
            table[n] = i
        return [-1, -1]