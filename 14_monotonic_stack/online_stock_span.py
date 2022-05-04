from math import inf


class StockSpanner:
    def __init__(self):
        self.stack = [(inf, 0)]  # price, cnt of days <= price

    # The span of the stock's price in one day is the maximum number of consecutive days (starting from that day (current day, inclusive) and going backward) for which the stock price was less than or equal to the price of that day.
    # next: Returns the span of the stock's price given that today's price.
    # e.g. [7,2,1,2], price=2, span=4    [7,34,1,2], price=8, span=3
    def next(self, price: int) -> int:
        cnt = 0
        while self.stack[-1][0] <= price:
            cnt += self.stack.pop()[1] + 1
        self.stack.append((price, cnt))
        return cnt + 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
