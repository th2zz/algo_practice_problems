from heapq import heappop, heappush
from typing import List


class Solution:  # https://leetcode.cn/problems/find-k-pairs-with-smallest-sums
    # 因为输入均为排序数组 nums1[0], nums2[0] 必定为一组解
    # 我们可以由此联想出这种避免双重循环n^2 的写法
    # Time O(k log min(m, k))
    # Space O(min(m, k))
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        pq = [(nums1[0] + nums2[0], 0, 0)]  # (sum, idx_u, idx_v)
        res = []
        while pq and len(res) < k:
            _, i, j = heappop(pq)
            res.append([nums1[i], nums2[j]])
            # # j is at smallest possible pos, try all possible i if not out of bound
            if j == 0 and i + 1 < m:  
                heappush(pq, (nums1[i + 1] + nums2[0], i + 1, 0))
            if j + 1 < n:  # j + 1 not out of bound
                heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
        return res


# nums1 = [1, 7, 11]
# nums2 = [2, 4, 6]
# k = 3
# print(Solution().kSmallestPairs(nums1, nums2, k))
