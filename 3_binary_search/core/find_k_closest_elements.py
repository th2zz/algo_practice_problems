class Solution:
    """https://www.lintcode.com/problem/460/?_from=collection&fromId=161
    Description
    Given target, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers
    to target in A, sorted in ascending order by the difference between the number and target.
    Otherwise, sorted in ascending order by number if the difference is same.

    The value k is a non-negative integer and will always be smaller than the length of the sorted array.
    Length of the given array is positive and will not exceed 10^410
    ​4
    ​​
    Absolute value of elements in the array will not exceed 10^410
    ​4
    ​​
    Example
    Example 1:

    Input: A = [1, 2, 3], target = 2, k = 3
    Output: [2, 1, 3]
    Example 2:

    Input: A = [1, 4, 6, 8], target = 3, k = 3
    Output: [4, 1, 6]
    Challenge
    O(logn + k) time
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A: list, target: int, k: int):  # target可以在A中也可以不在   找到最接近target的两个数
        right = self.find_least_upper_bound_of_target(A, target)  # TODO 需要注意！
        left = right - 1
        results = []
        for _ in range(k):   # 两根指针背向而行 merge sorted array直到找到k个数为止; 此处判断有序标准为 "距离target是否更近"
            if self.left_closer_to_target(A, target, left, right):  # 选择更近的 left or right
                results.append(A[left])
                left -= 1
            else:
                results.append(A[right])
                right += 1
        return results

    def left_closer_to_target(self, A, target, left, right):
        # 将merge2sorted array中 对于越界的检查 封装到 这个判断距离的metric中
        if left < 0:  # 左边越界 找右边
            return False
        if right >= len(A):  # 右边越界 找左边
            return True
        return target - A[left] <= A[right] - target  # 没越界 返回实际情况 左边近不近

    def find_least_upper_bound_of_target(self, A, target):
        # find least upperbound
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target:  # a[mid] is an upperbound, lower right bound to find better result
                end = mid
            else:  # a[mid] is not an upperbound, increase left bound to make a[mid] larger
                start = mid
        if A[start] >= target:  # 因为需要找最左数 这里先判断start
            return start
        if A[end] >= target:
            return end
        return len(A)  # TODO 返回len(A) 让left = len(A) - 1

res =Solution().kClosestNumbers([1,2,3], 2, 3)
print(res)