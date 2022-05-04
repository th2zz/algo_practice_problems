from typing import (
    List,
)

class Solution:
    """https://www.lintcode.com/problem/1879/?fromId=161&_from=collection
Description
Given an array of integers that is already sorted in ascending order of absolute value, find two numbers so that the sum of them equals a specific number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Note: the subscript of the array starts with 0

You are not allowed to sort this array.

It is guaranteed that all numbers in the numsnums is distinct.
The length of numsnums is \leq 100\,000≤100000.
The number in numsnums is \leq 10^9≤10
9
 .
Example
Input:
[0,-1,2,-3,4]
1
Output:
[[1,2],[3,4]]
Explanation:
nums[1] + nums[2] = -1 + 2 = 1, nums[3] + nums[4] = -3 + 4 = 1
You can return [[3,4],[1,2]], the system will automatically help you sort it to [[1,2],[3,4]]. But [[2,1],[3,4]] is invaild.
Challenge
\mathcal{O}(n)O(n) time complexity and \mathcal{O}(1)O(1) extra space

Tags
Same Direction Two Pointers
Two Pointers
Related Problems
689
Two Sum IV - Input is a BST
Medium
608
Two Sum II - Input array is sorted
Medium
610
Two Sum - Difference equals to target
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
533
Two Sum - Closest to target
Medium
443
Two Sum - Greater than target
Medium
56
Two Sum
Easy
Recommend Courses
    @param nums: the input array
    @param target: the target number
    @return: return the target pair
             we will sort your return value in output
    """
    def two_sum_v_i_i(self, nums: List[int], target: int) -> List[List[int]]:
        # write your code here
        pass