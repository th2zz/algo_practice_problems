import collections
import heapq


class TopKChecker:
    def __init__(self, k):
        self.capacity = k
        self.q = []

    def add(self, item):
        heapq.heappush(self.q, item)
        if len(self.q) > self.capacity:
            heapq.heappop(self.q)  # evict 1 item from min heap

    def topK(self):
        return self.q  # in any order


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = collections.defaultdict(int)
        for num in nums:
            freq_table[num] += 1
        topk_checker = TopKChecker(k)
        for num, freq in freq_table.items():
            topk_checker.add((freq, num))
        res = topk_checker.topK()
        res = [item[1] for item in res]
        return res
