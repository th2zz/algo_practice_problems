class Solution:
    """https://www.lintcode.com/problem/457/?_from=collection&fromId=161
    Find any position of a target number in a sorted array. Return -1 if target does not exist.
    Input: nums = [1,2,2,4,5,5], target = 2
    Output: 1 or 2
    Input: nums = [1,2,2,4,5,5], target = 6
    Output: -1
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    eqivalent to find first pos of target
    """

    def findPosition(self, nums, target):
        if not nums:
            return -1
        n = len(nums)
        start, end = 0, n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        # find first pos  check start first      start end next to each other
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1


print(Solution().findPosition([1, 2, 2, 4, 5, 5], 2))
print(Solution().findPosition([1, 2, 2, 4, 5, 5], 6))
