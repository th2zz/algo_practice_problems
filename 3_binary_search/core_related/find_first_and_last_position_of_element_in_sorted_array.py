class Solution:
    # https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
    def find_first_pos_of_target(self, nums: List[int], target: int)->int:
        if not nums:
            return -1
        start,end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
    
    def find_last_pos_of_target(self, nums: List[int], target: int)->int:
        if not nums:
            return -1
        start,end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        return [self.find_first_pos_of_target(nums, target), self.find_last_pos_of_target(nums, target)]
        