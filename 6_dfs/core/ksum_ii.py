class Solution:
    """https://www.lintcode.com/problem/90/?_from=collection&fromId=161
Given n unique postive integers, number k (1<=k<=n1<=k<=n) and target.
Find all possible k integers where their sum is target.

Example 1:

Input:
array = [1,2,3,4]
k = 2
target = 5
Output:
[[1,4],[2,3]]
Explanation:

1+4=5,2+3=5

Example 2:

Input:

array = [1,3,4,6]
k = 3
target = 8
Output:

[[1,3,4]]
Explanation:

1+3+4=8
    @param A: an integer array 假设无重复
    @param k: a postive integer <= length(A)
    @param targer: an integer
    @return: A list of lists of integer  给定长度为n的int数组A, 找到所有满足 ksum = target的无重复组合 (subsequence)
    """

    def k_sum_i_i(self, a: list[int], k: int, target: int) -> list[list[int]]:
        if not a:  # no need to sort because we are not following lexicographical order and no duplication is assumed
            return []
        res = []
        self.dfs(a, 0, k, target, comb=[], res=res)
        return res

    def dfs(self, a, index, k, target, comb, res):  # 递归的定义 从a[index]开始 找到以comb为前缀的  k sum to target的所有完整组合
        if k == 0 and target == 0:
            res.append(list(comb))  # 递归的出口 deep copy
            return
        if (k == 0 and target != 0) or (k != 0 and target <= 0):  # 可行性剪枝 + 不合法的出口
            return
        for i in range(index, len(a)):  # 递归的拆解和递进  在当前位置上逐个尝试 增加a中任意一个数到comb 判断能否找到k sum to target 能找到则加到结果集
            comb.append(a[i])  # include a[i] and dfs recurse on sub problem
            self.dfs(a, i + 1, k - 1, target - a[i], comb, res)  # i + 1代表不能重复的选; 子问题是k-1 sum to target - A[i] starting from a[i + 1]
            comb.pop()  # backtrack recent action 尝试新的a[i]
