from typing import (
    List,
)
"""
Algorithms
Medium
Accepted Rate
37%

DescriptionSolutionNotesDiscussLeaderboard
This topic is a pre-release topic. If you encounter any problems, please contact us via "Problem Correction", and we will upgrade your account to VIP as a thank you.
Description
Given n items with size A_{i}A 
i
​
  an integer m denotes the size of a backpack. How full you can fill this backpack?
(Each item can only be selected once and the size of the item is a positive integer)

You can not divide any item into small pieces.
n \lt 1000n<1000
m \lt 1e9m<1e9
Example
Example 1:

Input:

array = [3,4,8,5]
backpack size = 10
Output:

9
Explanation:

Load 4 and 5.

Example 2:

Input:

array = [2,3,5,7]
backpack size = 12
Output:

12
Explanation:

Load 5 and 7.

Tags
Backpack DP
Dynamic Programming/DP
Related Problems
1538
Card Game II
Medium
800
Backpack IX
Medium
749
John's backyard garden
Easy
724
Minimum Partition
Medium
700
Cutting a Rod
Medium
669
Coin Change
Medium
588
Partition Equal Subset Sum
Medium
564
Combination Sum IV
Medium
563
Backpack V
Medium
562
Backpack IV
Medium
440
Backpack III
Medium
279
Number of Ways to Represent N Cents
Medium
125
Backpack II
Medium
"""
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, m: int, a: List[int]) -> int:
        # write your code here
        pass