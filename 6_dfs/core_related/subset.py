from typing import (
    List,
)


class Solution:
    """ https://www.lintcode.com/problem/17/?_from=collection&fromId=161
    Medium
    Given a set with distinct integers, return all possible subsets.

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Example
Example 1:

Input:

nums = [0]
Output:

[
  [],
  [0]
]
Explanation:

The subsets of [0] are only [] and [0].

Example 2:

Input:

nums = [1,2,3]
Output:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
Explanation:

The subsets of [1,2,3] are [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3].

Challenge
Can you do it in both recursively and non-recursively?
TAGS: DFS
Related Problems
1210
Increasing Subsequences
Medium
935
Cartesian Product
Medium
761
Smallest Subset
Medium
730
Sum of All Subsets
Easy
680
Split String
Medium
426
Restore IP Addresses
Medium
18
Subsets II
Medium
            []  搜索的起点
        /   |    \
       1    2     3
     /  \   /\    /\
    12  13 21 23 31 32

    123 132 213 231 312 321  叶子层

求所有子集 需要把搜索树上所有节点都放到结果集中
    @param nums: A set of numbers
    @return: A list of lists 给定一个数字集合 返回所有可能的子集
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        result = []
        self.dfs(sorted(nums), 0, comb=[], result=result)  # TODO 需要排序 搜索树是按序选择的!
        return result

    # 递归的定义 从nums[idx]开始 找到前缀为comb的 所有组合
    # 递归的拆解和递进 从nums[idx]开始 逐个尝试当前元素作为 下个元素  进行递归调用 求解 下个位置(i+1)位置开始 以新的comb为前缀的所有组合 递归调用结束后回溯comb
    # 递归的出口 出口就是 枚举完 找到了所有搜索树上的点
    def dfs(self, nums, idx, comb, result):  # 可以认为idx==len(comb) 也是 comb的下一个位置
        result.append(list(comb))  # deep copy
        for i in range(idx, len(nums)):
            comb.append(nums[i])
            self.dfs(nums, i + 1, comb, result)  # comb[idx]位置已经被固定为nums[i] 递归调用考虑的子问题是  "从下个位置开始 找到以新的comb为前缀的所有组合"
            comb.pop()  # 选完1后 只考虑增加2 或 3 新的节点为12 或 13;                 求解完上述子问题后 backtrack comb尝试新的元素作为下个元素
