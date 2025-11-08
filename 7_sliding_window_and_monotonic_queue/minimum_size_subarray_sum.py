from typing import List


class Solution:
    # https://leetcode.cn/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150
    # find minimal length of contiguous subarray that sum to >= target
    # e.g. [2,3,1,2,4,3] target=7 => [4,3]
    # [1,4,4] target =4 => 4
    # [1,1,1,1,1,1,1,1] target = 11 => 0
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        res, n = len(nums) + 1, len(nums)
        r = 0
        curr_sum = 0
        for l in range(n):
            if l > 0:
                curr_sum -= nums[l - 1]  # remove it out of window
            # r explore and try to find a sum >= target
            while r in range(n) and curr_sum < target:
                curr_sum += nums[r]
                r += 1  # r is the pos after the pos caused last curr_sum change
            if curr_sum >= target:
                res = min(res, r - l)
        return res if res <= n else 0


print(Solution().minSubArrayLen(target=4, nums=[1, 4, 4]))
