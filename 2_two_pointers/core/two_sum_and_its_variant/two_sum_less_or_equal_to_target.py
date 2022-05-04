# Input: nums = [2, 7, 11, 15], target = 24.
# Output: 5.
# Explanation:
# 2 + 7 < 24
# 2 + 11 < 24
# 2 + 15 < 24
# 7 + 11 < 24
# 7 + 15 < 24

# Input: nums = [1], target = 1.
# Output: 0.


class Solution:
    """https://www.lintcode.com/problem/609/?_from=collection&fromId=161
    Description
Given an array of integers, find how many pairs in the array such that their sum is less than or equal to a specific
target number. Please return the number of pairs.

Example
Example 1:

Input: nums = [2, 7, 11, 15], target = 24.
Output: 5.
Explanation:
2 + 7 < 24
2 + 11 < 24
2 + 15 < 24
7 + 11 < 24
7 + 15 < 24
Example 2:

Input: nums = [1], target = 1.
Output: 0.
Tags
Opposite Direction Two Pointers
Two Pointers
Related Problems
1879
Two Sum VII
Hard
1796
K-Difference
Medium
689
Two Sum IV - Input is a BST
Medium
608
Two Sum II - Input array is sorted
Medium
610
Two Sum - Difference equals to target
Medium
607
Two Sum III - Data structure design
Easy
587
Two Sum - Unique pairs
Medium
533
Two Sum - Closest to target
Medium
443
Two Sum - Greater than target
Medium
56
Two Sum
Easy

    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    naive brute force takes O(n^2) two pass
    O(nlogn) O(1)
    """
    def twoSum5(self, nums, target):
        nums.sort()  # TODO remember to sort
        count, left, right = 0, 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1 # decrease sum
            else:
                count += right - left # index @ left,...,right - 1  add them in batch
                left += 1 # increase sum
        return count
