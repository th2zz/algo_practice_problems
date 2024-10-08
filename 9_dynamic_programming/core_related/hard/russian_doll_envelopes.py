from typing import (
    List,
)
"""
Description
Give a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.
Find the maximum number of nested layers of envelopes.

Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)


Example
Example 1:

Input：[[5,4],[6,4],[6,7],[2,3]]
Output：3
Explanation：
the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
Example 2:

Input：[[4,5],[4,6],[6,7],[2,3],[1,1]]
Output：4
Explanation：
the maximum number of envelopes you can Russian doll is 4 ([1,1] => [2,3] => [4,5] / [4,6] => [6,7]).
Tags
Dynamic Programming/DP
Coordinate DP
Company
Facebook
Google
"""
class Solution:
    """
    @param envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def max_envelopes(self, envelopes: List[List[int]]) -> int:
        pass
