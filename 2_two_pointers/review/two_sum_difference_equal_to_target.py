from typing import (
    List,
)
"""
Algorithms
Medium
Accepted Rate
37%

https://www.lintcode.com/problem/610/?fromId=161&_from=collection
Description
Given an sorted array of integers, find two numbers that their difference equals to a target value.
Return a list with two number like [num1, num2] that the difference of num1 and num2 equals to target value, and num1 is less than num2.

It's guaranteed there is only one available solution.
Note: Requires O(1) space complexity to comple

Example
Example 1:

Input: nums = [2, 7, 15, 24], target = 5 
Output: [2, 7] 
Explanation:
(7 - 2 = 5)
Example 2:

Input: nums = [1, 1], target = 0
Output: [1, 1] 
Explanation:
(1 - 1 = 0)
Tags
Hash Table
Same Direction Two Pointers
Two Pointers
Related Problems
1879
Two Sum VII
Hard
1797
optimalUtilization
Easy
1187
K-diff Pairs in an Array
Easy
689
Two Sum IV - Input is a BST
Medium
608
Two Sum II - Input array is sorted
Medium
609
Two Sum - Less than or equal to target
Medium
607
Two Sum III - Data structure design
Easy
587
Two Sum - Unique pairs
Medium
443
Two Sum - Greater than target
Medium
56
Two Sum
Easy
"""

class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (index1 < index2)
    """
    def two_sum7(self, nums: List[int], target: int) -> List[int]:
        pass