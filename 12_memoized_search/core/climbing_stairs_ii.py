class Solution:
    """https://www.lintcode.com/problem/272/?_from=collection&fromId=161
easy
A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a \
method to count how many possible ways the child can run up the stairs.

For n=0, we think the answer is 1.

Example
Example 1:

Input: 3
Output: 4
Explanation: 1 + 1 + 1 = 2 + 1 = 1 + 2 = 3 = 3 , there are 4 ways.
Example 2:

Input: 4
Output: 7
Explanation: 1 + 1 + 1 + 1 = 1 + 1 + 2 = 1 + 2 + 1 = 2 + 1 + 1 = 2 + 2 = 1 + 3 = 3 + 1 = 4 , there are 7 ways.
Tags
Dynamic Programming/DP
Coordinate DP
    @param n: An integer a staircase with n steps
    @return: An Integer how many possible ways the child can run up the stairs.
    """

    def climbStairs2(self, n):
        if n <= 1:
            return 1
        num_ways = [1] * (n + 1)
        # num_ways = [1, 1, 2, 4] + [0] * (n - 3)
        for i in range(1, len(num_ways)):
            num_ways[i] = num_ways[i - 1]
            if i >= 2:
                num_ways[i] += num_ways[i - 2]
            if i >= 3:
                num_ways[i] += num_ways[i - 3]
        return num_ways[n]


print(Solution().climbStairs2(3))
print(Solution().climbStairs2(4))
