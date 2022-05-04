class Solution:
    """https://www.lintcode.com/problem/603/?_from=collection&fromId=161
    Algorithms
Medium
Accepted Rate
41%

DescriptionSolutionNotesDiscussLeaderboard
Description
Given a set of distinct positive integers, find the largest subset which has the most elements,
and every pair of two elements (Si, Sj) in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.
1 \leq len(nums) \leq 500001≤len(nums)≤50000

Example
Example 1:

Input: nums =  [1,2,3],
Output: [1,2] or [1,3]
Example 2:

Input: nums = [1,2,4,8],
Output: [1,2,4,8]
Tags
Dynamic Programming/DP
Coordinate DP
Company
Google
Related Problems
76
Longest Increasing Subsequence
Medium

    @param nums: a set of distinct positive integers
    @return: the largest subset s.t. every pair of integers is divisible one way or the other
    """

    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        nums = sorted(nums)  # dp[i] size of largest divisible subset ending with i
        dp, prev = {x: 1 for x in nums}, {x: -1 for x in nums}  # prev is used to restore path
        last_num = nums[0]  # last number and largest number in subset
        for x in nums:
            for factor in self.get_factors(x):
                if factor not in dp:
                    continue
                if dp[x] < dp[factor] + 1:  # factor < x;  dp[x] = max(dp[x's factor]) + 1; +1 = include x to subset
                    dp[x] = dp[factor] + 1
                    prev[x] = factor  # record path
            if dp[x] > dp[last_num]:
                last_num = x
        return self.get_path(prev, last_num)

    # O(sqrt(n)) get all factors of x, excluding x itself
    def get_factors(self, x):
        if x == 1:
            return []
        factor = 1
        factors = []
        while factor * factor <= x:  # 分界线是 sqrt(x) ; 只需要遍历一半
            if x % factor == 0:
                factors.append(factor)  # 放上这个因子
                if factor * factor != x and factor != 1:  # 不重复 不为1
                    factors.append(x // factor)  # 放上另一半
            factor += 1
        return factors

    # restore path with prev dict start from last_num
    def get_path(self, prev, last_num):
        path = []
        while last_num != -1:
            path.insert(0, last_num)
            last_num = prev[last_num]
        return path
