class Solution:
    """
    https://www.lintcode.com/problem/144/
    Description
    Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.

    You are not necessary to keep the original order of positive integers or negative integers.

    Example
    Example 1

    Input : [-1, -2, -3, 4, 5, 6]
    Outout : [-1, 5, -2, 4, -3, 6]
    Explanation :  any other reasonable answer.
    Challenge
    Do it in-place and without extra memory.
    @param: A: An integer array.
    @return: nothing

    可行解

- 先全部排序
  - 没有必要 只需要把正负分开
- 再正负交错
- 已知数据确保正负数相差个数不超过1  正数还是负数多有关系吗 有关系  partition后只需要处理相等数量正数负数 同向双指针交换一组后各前进2步
  - 负数多 左负右正after partition; left =1, right = length - 1 跳过开始的负数 间隔交换
  - 正数多 left = 0, right = length - 2 跳过最后的正数 间隔交换
  - 一样 left = 0, right = length - 1 间隔交换

    """
    def rerange(self, A):
        # O(n) O(1)
        # 输入是否有序 不是
        # 有没有重复数字 影响不大
        # 已知数据确保正负数相差个数不超过1
        # 不需要额外空间
        # 不需要保持正数和负数原来的顺序
        # pos > neg   left = 0, right = len(A) - 2 右边错开1位
        # neg > pos   left = 1, right = len(A) - 1 左边错开1位  # TODO 哪边元素多哪边向内部错开1位
        # neg = pos   left = 0, right = len(A) - 1 对称
        neg_cnt = self.partition(A, 0)  # left 是>= 0 的开始
        pos_cnt = len(A) - neg_cnt
        left = 1 if neg_cnt > pos_cnt else 0  # 根据奇偶情况做一个同向双指针interleave TODO 保证两边开始位置 是等距的
        right = len(A) - 2 if pos_cnt > neg_cnt else len(A) - 1
        self.interleave(A, left, right)

    def partition(self, A, target):
        #  after partition two sublists = [start...right]?[left...end]  left 和 right中间有可能还有一个数, left != right
        left, right = 0, len(A) - 1
        while left <= right:
            while left <= right and A[left] < target:
                left += 1
            while left <= right and A[right] > target:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        return left

    def interleave(self, A, left, right):  # TODO interleave做的就算根据上面错开的left, right 相向双指针 swap后 同步+2-2
        while left < right:
            A[left], A[right] = A[right], A[left]
            left += 2
            right -= 2
