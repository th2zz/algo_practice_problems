from typing import (
    List,
)
"""
Algorithms
Medium
Accepted Rate
38%

https://www.lintcode.com/problem/59/?fromId=161&_from=collection
Description
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example
Example 1:

Input:

numbers = [2,7,11,15]
target = 3
Output:

20
Explanation:

2+7+11=20
Example 2:

Input:

numbers = [-1,2,1,-4]
target = 1
Output:

2
Explanation:

-1+2+1=2

Challenge
O(n^2)O(n 
2
 ) time, O(1)O(1) extra space

Tags
Hash Table
Opposite Direction Two Pointers
Two Pointers
Enumerate
Related Problems
918
3Sum Smaller
Medium
533
Two Sum - Closest to target
Medium
57
3Sum
Medium
56
Two Sum
Easy
Recommend Courses
"""
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def three_sum_closest(self, numbers: List[int], target: int) -> int:
        # write your code here
        pass