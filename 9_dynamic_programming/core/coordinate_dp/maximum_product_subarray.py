# https://leetcode-cn.com/problems/maximum-product-subarray/
class Solution:  # same as max sum contiguous subarray, but we want max product
    def maxProduct(self, nums: list[int]) -> int:  # nums unsorted, can have negative / positive numbers
        if not nums:
            return 0
        maxf = [0] * len(nums)  # maxf[i] max product ends at position i
        minf = [0] * len(nums)  # minf[i] min product ends at position i, this helps to record negative products at previous pos
        minf[0] = nums[0]
        maxf[0] = nums[0]
        max_product = maxf[0]
        for i in range(1, len(nums)):  # minf[i-1]*nums[i] can be new max when previous product is negative and nums[i] < 0
            maxf[i] = max(maxf[i - 1] * nums[i], minf[i - 1] * nums[i], nums[i])
            minf[i] = min(maxf[i - 1] * nums[i], minf[i - 1] * nums[i], nums[i])
            max_product = max(max_product, maxf[i])
        return max_product


print(Solution().maxProduct([-2, 3, -4]))
