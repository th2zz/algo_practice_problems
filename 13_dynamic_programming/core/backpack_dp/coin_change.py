# https://leetcode-cn.com/problems/coin-change/
import sys


class Solution:
    """
给定一个硬币列表, 一个amount (int), 找到凑够amount的最少硬币数, 不能凑出来返回-1, 假设每种硬币数量无限
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        if not amount:
            return 0
        # num_coins[i]:= minimum #coins needed for amount i
        # num_coins[i] = 0 if i == 0, nums_coins[i] = -1 if i < 0
        # num_coins[i] = 1 + min(nums_coin[i - coin]) for each coin in coins
        num_coins = [sys.maxsize if i >= 1 else 0 for i in range(amount + 1)]
        for am in range(1, amount + 1):  # i depends on smaller i
            for c in coins:
                if c > am:
                    continue
                num_coins[am] = min(num_coins[am], 1 + num_coins[am - c])
        return num_coins[amount] if num_coins[amount] != sys.maxsize else -1
