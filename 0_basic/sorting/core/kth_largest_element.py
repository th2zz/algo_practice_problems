class Solution:  # https://leetcode.cn/problems/kth-largest-element-in-an-array/
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k < 1 or k > len(nums):
            return None
        # len(nums) - k : 可以直接当作第索引使用 找到索引为len(nums) - k的元素
        # e.g. 5 elements find 2th largest = find 4th smallest = find item at index 3
        # 3 = 5 - 2
        return self.quick_select(nums, 0, len(nums) - 1, len(nums) - k)

    def quick_select(self, nums: List[int], start: int, end: int, k: int) -> int:
        if start == end:
            return nums[start]
        # 此时 two sublists = [start...right]?[left...end]  # left, right中间要么没有要么有一个数, left != right
        left, right = self.partition(nums, start, end, k)
        if k <= right:
            return self.quick_select(nums, start, right, k)
        if k >= left:
            return self.quick_select(nums, left, end, k)
        return nums[k]  # right < k < left    pivot 循环结束此时中间有一个数 +1-1错开1位

    def partition(self, nums: List[int], left: int, right: int, k: int) -> int:
        pivot = nums[(left + right) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left, right  # [start right <= pivot] [left end >= pivot]
