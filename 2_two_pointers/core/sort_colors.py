class Solution:
    """148
    Description
    Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
    with the colors in the order red, white and blue.

    We will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
    [0...][1...][2...]
    You are not suppose to use the library's sort function for this problem.
    You should do it in-place (sort numbers in the original array).

    Example
    Example 1

    Input : [1, 0, 1, 2]
    Output : [0, 1, 1, 2]
    Explanation : sort it in-place

    Challenge
    Could you come up with an one-pass algorithm using only O(1) space?
    SORT COLORS IN PLACE
    DO IT IN O(N) O(1) ?
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing, sort it in place

    [0, 1, 2, 0, 2, 1, 1] => [0, 0, 1, 1, 1, 2, 2]

- naive: sort it, O(NlogN) O(1)
- counting sort  O(N) O(1)
- quick partition
  - two pass partition array by 1, then by 2
  - one pass 0丢左边 2丢右边 1放中间   too complicated, not good for production
  彩虹排序 一个数组里有3中颜色 0 1 2  O(n) O(1) 完成排序 使得同颜色 相邻
    """

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def sortColors_counting_sort(self, nums):
        # - 计数排序 统计每种颜色出现次数
        # - 根据统计结果覆盖原数组
        if not nums:
            return
        color_cnts = [0] * 3  # init table
        for num in nums:
            color_cnts[num] += 1  # count frequency of 0, 1, 2 resp.
        p = 0  # ptr to original array
        for i in range(3):
            for cnt in range(color_cnts[i], 0, -1):
                nums[p] = i  # reconstruction: fill in original array
                p += 1

    def sortColors(self, nums):
        # 建议
        self.partition_arrays(nums, 1)
        self.partition_arrays(nums, 2)

    def partition_arrays(self, nums, k):  # same as problem partition_array, no need to swap pivot element to middle
        if not nums:
            return 0
        start, end = 0, len(nums) - 1
        pivot = k
        i, j = start, start
        for j in range(start, end + 1):
            if nums[j] < pivot:
                self.swap(nums, i, j)
                i += 1
        return i

    def sortColors_one_pass(self, nums):
        # onepass工程角度不推荐 可读性差
        zeroPt = -1
        twoPt = len(nums)
        i = 0
        # i < twoPt 是个很重要的条件
        while i < len(nums) and i < twoPt:
            if nums[i] == 0:
                zeroPt += 1
                nums[zeroPt], nums[i] = nums[i], nums[zeroPt]
                # 没有i-- 因为换过来的只可能是1 不需要再交换了
                # 当前指针左边不可能有2 所有的0也都小于zeroPt +1前的位置
            elif nums[i] == 2:
                twoPt -= 1
                nums[twoPt], nums[i] = nums[i], nums[twoPt]
                i -= 1
            i += 1
