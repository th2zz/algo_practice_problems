class Solution:
    """https://www.lintcode.com/problem/539/?_from=collection&fromId=161
    Description
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
Example
Example 1:

Input: nums = [0, 1, 0, 3, 12],
Output: [1, 3, 12, 0, 0].
Example 2:

Input: nums = [0, 0, 0, 3, 1],
Output: [3, 1, 0, 0, 0].
Tags
Opposite Direction Two Pointers
Two Pointers
Array
Company
Facebook
Related Problems
172
Remove Element
Easy

    0丢到数组末尾 in place, minimize total# operations (一般理解为write operations)
    - 同向双指针 填充指针指向将被填充的非0位置 前移指针explorer 指向要被填充的非0数
    - minimize write by not swapping & clear remaining with 0

    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes_naive(self, nums):
        fill_ptr = 0
        for move_ptr in range(len(nums)):
            if nums[move_ptr] != 0:
                # 不等于才有交换意义
                if fill_ptr != move_ptr:
                    nums[fill_ptr], nums[move_ptr] = nums[move_ptr], nums[fill_ptr]
                fill_ptr += 1

    def moveZeroes(self, nums):
        # minimize write operations by not swapping
        fill_ptr = 0
        for move_ptr in range(len(nums)):
            if nums[move_ptr] != 0:
                if fill_ptr != move_ptr:
                    nums[fill_ptr] = nums[move_ptr]
                fill_ptr += 1
        # 把后续所有数字清零
        for i in range(fill_ptr, len(nums)):
            nums[i] = 0
