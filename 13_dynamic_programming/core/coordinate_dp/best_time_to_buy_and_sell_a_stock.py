import sys


class Solution:
    # https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
    def maxProfit(self, prices: List[int]) -> int:  # can only sell after day 1, cannot buy and sell on the same day
        if not prices:
            return 0
        dp = [0] * len(prices)  # max profits at day i
        min_prices = [sys.maxsize] * len(prices)  # min_price at day i, same idea as prefix prefix_array
        min_price = sys.maxsize
        for i, p in enumerate(prices):
            min_price = min(p, min_price)
            min_prices[i] = min_price
        for i in range(1, len(dp)):
            dp[i] = max(dp[i - 1], prices[i] - min_prices[i - 1])
        return dp[len(prices) - 1]  # return max profits at the last day

    def maxProfit2(self, prices: List[int]) -> int:  # optimized version with rolling variable
        if not prices:
            return 0
        max_profits = 0  # if you cannot achieve any profits return 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            max_profits = max(max_profits, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return max_profits
