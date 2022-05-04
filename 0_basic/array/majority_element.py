import collections
from random import randrange


class Solution:
    def count(self, nums, num):
        cnt = 0
        for n in nums:
            if n == num:
                cnt += 1
        return cnt

    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        n = len(nums)
        rand_idx = randrange(n)
        while self.count(nums, nums[rand_idx]) <= n // 2:
            rand_idx = randrange(n)
        return nums[rand_idx]

    def majorityElement2(self, nums: List[int]) -> int:
        if not nums:
            return -1
        n = len(nums)
        rand_idx = randrange(n)
        ftable = collections.defaultdict(int)
        for num in nums:
            ftable[num] += 1
        while ftable[nums[rand_idx]] <= n//2:
            rand_idx = randrange(n)
        return nums[rand_idx]
