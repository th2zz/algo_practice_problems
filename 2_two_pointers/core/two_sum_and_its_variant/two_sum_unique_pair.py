class Solution:
    """
    Description
    Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.

    Example
    Example 1:

    Input: nums = [1,1,2,45,46,46], target = 47
    Output: 2
    Explanation:

    1 + 46 = 47
    2 + 45 = 47

    Example 2:

    Input: nums = [1,1], target = 2
    Output: 1
    Explanation:
    1 + 1 = 2
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        res = 0
        nums = sorted(nums)
        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                res += 1
                right -= 1
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif sum > target:
                right -= 1
            else:
                left += 1
        return res

# print(Solution().twoSum6([1,1,2,45,46,46], 47))
# print(Solution().twoSum6([1,1], 2))