from typing import (
    List,
)

class Solution:
    """https://www.lintcode.com/problem/465/?fromId=161&_from=collection
Description
Given two integer arrays sorted in ascending order and an integer k. Define sum = a + b, where a is an element from the first array and b is an element from the second one. Find the kth smallest sum out of all possible sums.

Example
Example 1

Input:
a = [1, 7, 11]
b = [2, 4, 6]
k = 3
Output: 7
Explanation: The sums are [3, 5, 7, 9, 11, 13, 13, 15, 17] and the 3th is 7.
Example 2

Input:
a = [1, 7, 11]
b = [2, 4, 6]
k = 4
Output: 9
Explanation: The sums are [3, 5, 7, 9, 11, 13, 13, 15, 17] and the 4th is 9.
Example 3

Input:
a = [1, 7, 11]
b = [2, 4, 6]
k = 8
Output: 15
Explanation: The sums are [3, 5, 7, 9, 11, 13, 13, 15, 17] and the 8th is 15.
Challenge
Do it in either of the following time complexity:

O(k log min(n, m, k)). where n is the size of A, and m is the size of B.
O( (m + n) log maxValue). where maxValue is the max number in A and B.
Tags
Same Direction Two Pointers
Heap
Binary Search on Answer
Binary Search
Two Pointers
Related Problems
401
Kth Smallest Number in Sorted Matrix
Medium
38
Search a 2D Matrix II
Medium
    @param a: an integer arrays sorted in ascending order
    @param b: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kth_smallest_sum(self, a: List[int], b: List[int], k: int) -> int:
        # write your code here
        pass