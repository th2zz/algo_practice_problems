# https://leetcode-cn.com/problems/maximum-subarray/


class Solution:  # find the contiguous subarray(len >= 1) that has the largest sum and return its sum
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return 0
        # f(i) = max(f(i - 1) + nums[i], nums[i])  i>= 1 # max sum of contiguous subarray ends at index i
        # f(0) = nums[0]
        f = [0] * len(nums)
        f[0] = nums[0]
        max_sum = f[0]
        for i in range(1, len(nums)):
            f[i] = max(
                f[i - 1] + nums[i], nums[i]
            )  # either include new num or start over from i
            max_sum = max(max_sum, f[i])
        return max_sum

    def maxSubArray2(self, nums: list[int]) -> int:  # rolling variable O(1) space
        if not nums:
            return 0
        max_sum_so_far = nums[0]
        max_sum = max_sum_so_far
        for i in range(1, len(nums)):
            max_sum_so_far = max(max_sum_so_far + nums[i], nums[i])
            max_sum = max(max_sum, max_sum_so_far)
        return max_sum


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
