from typing import (
    List,
)


class Solution:
    """ https://www.lintcode.com/problem/124  medium
Given an unsorted array num of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n)complexity.
len(num) <= 10000
Example 1:

Input:

num = [100, 4, 200, 1, 3, 2]
Output:

4
Explanation:

The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length:4

Tags
Hash Table
Related Problems
619
Binary Tree Longest Consecutive Sequence III
Medium
595
Binary Tree Longest Consecutive Sequence
Easy
    @param num: A list of integers
    @return: An integer  找到最长连续序列的长度

    枚举中心点 从中心点向两边扩散找最长连续序列 打擂台记录长度
    对于下一个中心点来说 他要么在之前找到的某个最长连续序列里 这样他不在unused中 要么是之前没遇到的 则会在unused中 可以以他为中心看下新的结果
    每个元素最多被删除1次 O(n)
    """

    def longest_consecutive(self, num: List[int]) -> int:
        unused = set(num)  # 用nums初始化一个set 记录未使用的数
        res = 0
        for item in num:  # 枚举中心点值
            if item in unused:  # 未使用 则 向(值)两侧扩散 找最长连续序列 并将沿途数从unused删除 打擂台记录最大长度
                unused.remove(item)
                l, r = item - 1, item + 1
                while l in unused:
                    unused.remove(l)
                    l -= 1
                while r in unused:
                    unused.remove(r)
                    r += 1
                res = max(res, r - l - 1)
        return res
