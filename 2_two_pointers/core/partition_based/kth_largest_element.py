class Solution:
    """ O(n) O(1)
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def quick_select(self, nums, start, end, k):
        # quick select k-th smallest element
        pivot_index = self.partition(nums, start, end)
        if k - 1 == pivot_index:
            return nums[pivot_index]
        elif k - 1 < pivot_index:
            return self.quick_select(nums, start, pivot_index - 1, k)
        else:
            return self.quick_select(nums, pivot_index + 1, end, k)

    def kthLargestElement(self, k, nums):
        if not nums:
            return -1
        if k > len(nums):
            return -1
        # k-th largest = "len(nums) + 1 - k"-th smallest
        return self.quick_select(nums, 0, len(nums) - 1, len(nums) + 1 - k)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def partition(self, nums, start, end):
        # or with randint [a,b] randrange [a, b)
        pivot_index = (start + end) // 2
        pivot = nums[pivot_index]
        self.swap(nums, pivot_index, end)
        i = start
        for j in range(start, end):
            if nums[j] < pivot:
                self.swap(nums, i, j)
                i += 1
        self.swap(nums, i, end)
        return i

    """ 解法2
    """

    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement2(self, k, A):
        if not A or k < 1 or k > len(A):
            return None
        # len(A) - k :: 可以直接当作第索引使用 找到索引为len(A) - k的元素
        return self.quick_select2(A, 0, len(A) - 1, len(A) - k)

    def partition2(self, nums, start, end):
        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
        return left, right  # [start right <= pivot] [left end >= pivot]

    def quick_select2(self, nums, start, end, k):
        """ find number indexed at k
        During the process, it's guaranteed start <= k <= end
        """
        if start == end:
            return nums[k]
        left, right = self.partition2(nums, start, end)  # left, right中间要么没有要么有一个数
        # 此时 two sublists = [start...right]?[left...end]  left 和 right中间有可能还有一个数, left != right
        if k <= right:
            return self.quick_select2(nums, start, right, k)
        if k >= left:
            return self.quick_select2(nums, left, end, k)
        return nums[k]  # right < k < left    pivot 循环结束此时中间有一个数 +1-1错开1位
