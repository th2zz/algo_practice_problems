class Solution:
    # https://leetcode.cn/problems/search-insert-position/
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if target > nums[end]:
            return end + 1
        if target < nums[start]:
            return start - 1 if start >= 1 else 0
        # now consider target present in array
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        # if target not present in array, insert at the last position
        return end