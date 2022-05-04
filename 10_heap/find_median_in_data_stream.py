from heapq import heappop, heappush


# 排序后的数组可以看成是大顶堆连上一个小顶堆，根据这个可以用两个堆来实现，这两个堆需要满足两个特性： 
# 1、大顶堆堆顶小于等于小顶堆堆顶。 
# 2、两个堆之间的元素个数相差不大于1。 假设我们始终让左边在奇数元素个数时比右边多一
# 所以当元素小于等于大顶堆堆顶时，push 进大顶堆，
# 元素大于大顶堆堆顶时， push 进小顶堆，便可以满足特性1，
# push后再判断两个堆的元素个数，如果两者相差超过 1，则需要平衡堆元素(pop后push)让条件2保持成立
# 返回中位数时 奇数取pql堆顶，偶数取两者对顶平均数.
class MedianFinder:
    # https://leetcode.cn/problems/find-median-from-data-stream/?envType=study-plan-v2&envId=top-interview-150
    def __init__(self):
        self.pql = []  # maxheap, assuming this always has 1 more item in case of odd number of total items
        self.pqr = []  # minheap

    def addNum(self, num: int) -> None:
        pql, pqr = self.pql, self.pqr
        if not pql or num <= -pql[0]:  # maxheap empty or item <= maxheap max
            heappush(pql, -num)
            # balance two q sizes to make invariant hold
            if len(pql) > len(pqr) and len(pql) - len(pqr) >= 2:
                heappush(pqr, -heappop(pql))
        else:  # pql and num > -pql[0]  maxheap nonempty and item larger than maxheap max
            heappush(pqr, num)
            # balance two q sizes;   pqr size <= pql size
            if len(pqr) > len(pql):
                heappush(pql, -heappop(pqr))

    def findMedian(self) -> float:
        pql, pqr = self.pql, self.pqr
        if len(pql) > len(pqr):
            return -pql[0]
        return (-pql[0] + pqr[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()