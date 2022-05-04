class Solution:
    """
    Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

Example
Example 1:

Input:

nums = []
k = 9
Output:

0
Explanation:

Empty array, print 0.

Example 2:

Input:

nums = [3,2,2,1]
k = 2
Output:

1
Explanation:

the real array is[1,2,2,3].So return 1.

Challenge
Can you partition the array in-place and in O(n)O(n)?
    @param nums: The integer array you should partition
    @param k: An integer
    @return: "partition the array based on pivot k, return partitioning index i: the first index i s.t. nums[i] >= k"
    """
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def partitionArray(self, nums, k):
        if not nums:
            return 0
        start, end = 0, len(nums) - 1
        # 没有必要像正常quick sort parition意义去取pivot index并交换至末尾/开始了
        # 因为对pivot位置没有限制! 只需要满足 left half < k; right half >= k 返回大半边的开始index
        # pivot_index = (start + end) // 2
        # self.swap(nums, pivot_index, end)
        pivot = k
        i, j = start, start
        # end + 1 因为pivot不在末尾了
        for j in range(start, end + 1):
            if nums[j] < pivot:
                # [< pivot |i][ >= pivot]
                self.swap(nums, i, j)
                # i goes to next to-be-swapped pos 始终存在于 确定有序的< pivot区间下一个位置
                i += 1
        # [< pivot][i| >= pivot]
        # pivot可以在nums中也可以不在 对pivot位置没有要求 不是在quick sort partition完要pivot在中间 因为pivot取自于数组
        # self.swap(nums, i, end)
        return i

    def partition_array(self, nums: list, k: int) -> int:  # TODO 为什么模板用 left <= right:  l ? r 的情况 下轮会重合 并退出循环 中间这个元素属于左还是右需要冗余的处理
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:  # TODO 和quick sort partition唯一区别在这 >= 题目要求 [< pivot][>= pivot]
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left  # [start...right][left...end]  返回右半边起点


# print(Solution().partitionArray([3,2,1], 2))
# 同向双指针partition法的一个变种 具体就是不需要取pivot了(当然也就不需要把pivot移动到末尾) 直接用给定的k  j的遍历range注意不再是去掉末尾的range 而是整个range
# 根据invariant 最后i的位置即右半>=pivot开始位置