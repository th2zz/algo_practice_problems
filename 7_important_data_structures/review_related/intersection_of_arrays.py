from typing import (
    List,
)


class Solution:
    """https://www.lintcode.com/problem/793/?fromId=161&_from=collection
Algorithms
Medium
Accepted Rate
59%

DescriptionSolutionNotesDiscussLeaderboard
Description
Give a number of arrays, find their intersection, and output their intersection size.

The total number of all array elements is not more than 500000.
There are no duplicated elements in each array.
Example
Example 1:

Input:  [[1,2,3],[3,4,5],[3,9,10]]
Output:  1

Explanation:
Only '3' in all three array.
Example 2:

Input: [[1,2,3,4],[1,2,5,6,7],[9,10,1,5,2,3]]
Output:  2

Explanation:
The set is [1,2].
Tags
Hash Table
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """

    def intersection_of_arrays(self, arrs: List[List[int]]) -> int:
        pass