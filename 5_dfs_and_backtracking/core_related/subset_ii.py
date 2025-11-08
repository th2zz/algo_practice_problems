from typing import (
    List,
)


class Solution:
    """ https://www.lintcode.com/problem/18/?_from=collection&fromId=161
    Medium
    Given a collection of integers that might contain duplicate numbers, return all possible subsets.

Each element in a subset must be in non-descending order.
The ordering between two subsets is free.
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

nums = [1,2,2]
Output:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
Explanation:

The distinct subsets of [1,2,2] are [], [1], [2], [1,2], [2,2], [1,2,2].

Challenge
Can you do it in both recursively and non-recursively?
Tags
Depth First Search/DFS
Related Problems
1210
Increasing Subsequences
Medium
730
Sum of All Subsets
Easy
680
Split String
Medium
17
Subsets
Medium

    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets. 同上题 但nums中可能有重复元素 找到所有无重复子集
    """

    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        res = []
        self.dfs(nums=sorted(nums), idx=0, comb=[], res=res, visited=[False] * len(nums))
        return res

    def dfs(self, nums, idx, comb, res, visited):
        res.append(list(comb))
        for i in range(idx, len(nums)):
            if visited[i]:  # 需要通过visited bitmap来知道选过什么 保证构造排列过程中 不重复选择 TODO 避免a1a1的情况
                continue
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:  # dedup & pruning, 选有代表性的, 不能跳过一个a选下一个a 不同位置同样的字符 必须按顺序使用 TODO 避免b1a2 a1b2的情况
                continue
            visited[i] = True
            comb.append(nums[i])
            self.dfs(nums, i + 1, comb, res, visited)
            comb.pop()
            visited[i] = False
