# https://leetcode-cn.com/problems/climbing-stairs/
class Solution:
    """
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
How many distinct ways can you climb to the top?

    """

    def climbStairs(self, n: int) -> int:
        # dp[i] = dp[i - 1] + d[i - 2] for i >= 2    dp[i]:= how many distinct ways to reach top in i steps
        # for i >= 0, i <= 1: dp[0] = 0, dp[1] = 1
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1  # define there is 1 way to reach top in 0 steps
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
