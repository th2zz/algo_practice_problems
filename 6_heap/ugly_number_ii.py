import heapq


class Solution:
    """https://www.lintcode.com/problem/4/?_from=collection&fromId=161
    Description
Ugly number is a number that only have prime factors 2, 3 and 5.

Design an algorithm to find the Nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

Note that 1 is typically treated as an ugly number.

1 <= n <= 10^5
5

Example 1:

Input:

n = 9
Output:

10
Explanation:

[1,2,3,4,5,6,8,9,10,....],the ninth ugly number is 10.

Example 2:

Input:

n = 1
Output:

1
Challenge
O(n log n) or O(n) time.

Tags
Dynamic Programming/DP
Heap
Mathmatics
Related Problems
518
Super Ugly Number
Medium
517
Ugly Number
Easy
    @param n: An integer
    @return: return a  integer as description.
丑数是 factor只为2, 3, 5的数 找到第n个丑数
前10个丑数是 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
    """

    def nthUglyNumber(self, n):  # 这题实际上是个bfs
        q = [1]  # min-heap to keep ugly numbers 优先队列 minheap 保证pop时数据有序
        visited = {1}  # visited set
        curr_ugly = 1
        for _ in range(n):  # 只做n次 pop 和 n次赋值
            curr_ugly = heapq.heappop(q)  # 小优化: 如果是最后一个丑数 可以不需要把乘积放到heap
            for factor in [2, 3, 5]:  # 生成新丑数方式是 分别* 2, 3, 5这三个factor 并入队
                new_ugly = curr_ugly * factor
                if new_ugly not in visited:
                    visited.add(new_ugly)  # 入队同时标记为已访问
                    heapq.heappush(q, new_ugly)
        return curr_ugly  # 第n个丑数

    # def nth_ugly_number(self, n: int) -> int:
    #     if n < 1:
    #         return -1
    #     q = [1]
    #     visited = {1}
    #     curr_ugly = 1
    #     while q:  # 可以去掉
    #         for _ in range(n):
    #             curr_ugly = heapq.heappop(q)
    #             for factor in [2, 3, 5]:
    #                 new_ugly = curr_ugly * factor
    #                 if new_ugly not in visited:
    #                     heapq.heappush(q, new_ugly)
    #                     visited.add(new_ugly)
    #         break  # 可以去掉
    #     return curr_ugly


print(Solution().nthUglyNumber(10))
