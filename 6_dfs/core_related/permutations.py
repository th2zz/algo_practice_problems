from typing import (
    List,
)


class Solution:
    """  https://www.lintcode.com/problem/15/?_from=collection&fromId=161
    Given a list of numbers, return all possible permutations of it.

You can assume that there is no duplicate numbers in the list.

Example
Example 1:

Input:

list = [1]
Output:

[
  [1]
]
Example 2:

Input:

list = [1,2,3]
Output:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
Challenge
Can you do it in both recursively and non-recursively?

Tags
Depth First Search/DFS
Related Problems
935
Cartesian Product
Medium
371
Print Numbers by Recursion
Medium
388
Permutation Sequence
Medium
16
Permutations II
Medium
    @param nums: A list of integers.
    @return: A list of permutations.  找到所有全排列 输入无重复
 求无重复全排列   数是可以逆序选的 所以不需要像组合一样 使用index做递归参数 从index开始往后看; e.g. [1,0] => [[1,0],[0,1]]
 但仍然需要去重 所以需要visited
"""

    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        res = []
        self.dfs(nums=nums, visited=[False] * len(nums), perm=[], res=res)
        return res

    def dfs(self, nums, visited, perm, res):
        if len(perm) == len(nums):
            res.append(list(perm))
            return
        for i in range(len(nums)):
            if visited[i]:  # 只需要一个去重剪枝
                continue
            perm.append(nums[i])
            visited[i] = True
            self.dfs(nums, visited, perm, res)
            visited[i] = False
            perm.pop()
