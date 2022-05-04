class Solution:  # https://leetcode-cn.com/problems/missing-number/
    # use XOR to find unique number
    # given nums containing n distinct numbers in range [0,n] return the only number missing  O(n) O(1)
    def missingNumber(self, nums: List[int]) -> int:  # 先把nums中所有数xor 再xor 0...n 即可获得只出现一次的数
        res = 0
        n = len(nums)
        for i, num in enumerate(nums):
            res ^= num
        for i in range(n + 1):
            res ^= i
        return res

    # another way is to calculate sum(0...n) - sum(nums) = n(n+1)/2 - sum(nums)
