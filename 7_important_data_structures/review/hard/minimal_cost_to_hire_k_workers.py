from typing import (
    List,
)

class Solution:
    """https://www.lintcode.com/problem/1512/?fromId=161&_from=collection
Description
There are N workers. The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group. When hiring a group of K workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.

1.1 <= K <= N <= 10000, where N = quality.length = wage.length
2.1 <= quality[i] <= 10000
3.1 <= wage[i] <= 10000
4.Answers within 10^-5 of the correct answer will be considered correct.

Example
Example 1:

Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.67
Explanation: We pay 4 to 0-th worker, 13.333 to 2-th and 3-th workers seperately.
Tags
Heap
Company
Google
    @param quality: an array
    @param wage: an array
    @param k: an integer
    @return: the least amount of money needed to form a paid group
    """
    def mincost_to_hire_workers(self, quality: List[int], wage: List[int], k: int) -> float:
        # Write your code here
        pass