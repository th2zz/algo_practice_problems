import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum2cnts = collections.defaultdict(int)
        if not nums:
            return 0
        sum = 0
        cnts = 0
        prefixsum2cnts[0] = 1
        # when sum == k, sum - k = 0, we may not have seen 0, but this still is a solution, so we have a special case
        for i, v in enumerate(nums):
            sum += v
            if sum - k in prefixsum2cnts:
                cnts += prefixsum2cnts[sum - k]
            prefixsum2cnts[sum] += 1
        return cnts
