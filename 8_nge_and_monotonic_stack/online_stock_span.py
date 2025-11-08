from math import inf

# https://leetcode.cn/problems/online-stock-span/solutions/1906765/gu-piao-jie-ge-kua-du-by-leetcode-soluti-5cm7/?envType=study-plan-v2&envId=leetcode-75
# The span of the stock's price in one day is the maximum number of consecutive days (starting from that day (current day, inclusive) and going backward) for which the stock price was less than or equal to the price of that day.
# next: Returns the span of the stock's price given that today's price.
# e.g. [7,2,1,2], price=2, span=4    [7,34,1,2], price=8, span=3
"""
调用 next 时，输入是新的一天的股票价格，需要返回包含此日在内的，
往前数最多有连续多少日的股票价格是小于等于今日股票价格的。
如果把每日的 price 当成数组不同下标的值，即需要求出每个值与上一个更大元素之间的下标之差。
这种题目可以用单调栈求解，具体原理可以参考「496. 下一个更大元素 I 的官方题解的方法二」。
此题的具体解法上，栈的元素可以是股票价格的下标（即天数）和股票价格的二元数对，
并且在栈中先插入一个最大值作为天数为 −1 天的价格，来保证栈不会为空。
调用 next 时，先将栈中价格小于等于此时 price 的元素都弹出，直到遇到一个大于 price 的值，并将 price 入栈，计算下标差返回。

"""


class StockSpanner:
    def __init__(self):
        self.stack = [(-1, inf)]
        self.idx = -1

    def next(self, price: int) -> int:
        self.idx += 1
        while price >= self.stack[-1][1]:
            self.stack.pop()
        self.stack.append((self.idx, price))
        return self.idx - self.stack[-2][0]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
