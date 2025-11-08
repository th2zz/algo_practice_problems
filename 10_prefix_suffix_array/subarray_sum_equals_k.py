import collections

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

#sum - k means
#  [sum - k][k] how many previous subarray of prefix sum sum - k we have seen? let's imagine we pick one, then sum - (sum - k) = k, the segment between that and current point constitute as one solution that sums to k, so #previous solutions should be added to #final solutions
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum2cnts = collections.defaultdict(int)
        if not nums:
            return 0
        sum = 0
        cnts = 0
        # maintain a {prefix_sum_up_to_i (inclusive) : #subarrays so far that sums to k} mapping
        prefixsum2cnts[0] = 1
        # when sum == k, sum - k = 0, we may not have seen 0, but this still is a solution, so we have a special case
        for _, v in enumerate(nums):
            sum += v
            if sum - k in prefixsum2cnts:  # 曾经有哪些subarray前缀和是sum-k，直接将这些前缀和出现频次加到解cnts中
                cnts += prefixsum2cnts[sum - k]
            prefixsum2cnts[sum] += 1
        return cnts
