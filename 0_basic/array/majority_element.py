import collections
from random import randrange


class Solution:
    # The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
    # enumerate item randomly and count until find a majority element
    # worst case O(inf), on-average O(n) because expected number of tries is 2, each try we count with O(n), space O(1)
    def count(self, nums, num):  # cnt num in nums
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
        while ftable[nums[rand_idx]] <= n // 2:
            rand_idx = randrange(n)
        return nums[rand_idx]
