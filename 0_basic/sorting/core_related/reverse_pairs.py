class Solution:
    """https://www.lintcode.com/problem/532/
    Description
Two numbers in the array, if the previous number is greater than the following number, then the two numbers form a reverse order pair. Give you an array, find out the total number of reverse order pairs in this array.
Summary: if a [i] > a [j] and i < j, a [i] and a [j] form a reverse order pair.

Example
Example1

Input:  A = [2, 4, 1, 3, 5]
Output: 3
Explanation:
(2, 1), (4, 1), (4, 3) are reverse pairs
Example2

Input:  A = [1, 2, 3, 4]
Output: 0
Explanation:
No reverse pair
Tags
Sort
Array
Divide and Conquer
Company
NetEase
Google
merge的过程中数横跨左右数组的逆序对 if A[left] > A[right] cnt += mid - left + 1;
    """
    # @param {int[]} A an array
    # @return {int} total of reverse pairs
    def reversePairs(self, A):
        # Write your code here
        self.tmp = [0 for _ in range(len(A))]
        return self.merge_sort(A, 0, len(A) - 1)

    def merge_and_count(self, A, start, end, mid, cnt):
        left, right, index = start, mid + 1, start  # [left...mid] [mid + 1, end]
        # 用一个指针去指引着填充 否则用数组append会重复添加, 而且需要copy back tmp's content to a
        while left <= mid and right <= end:
            if A[right] < A[left]:  # left smallest element > right smallest element; LEFT RIGHT SUBLISTS ALL SORTED
                self.tmp[index] = A[right]
                right += 1
                # add count! the full left sublist [left,mid] 都和right构成逆序对 批量计数
                cnt += mid - left + 1
            else:
                self.tmp[index] = A[left]
                left += 1
            index += 1  # WRITE PTR FOR TMP array
        while left <= mid:
            self.tmp[index] = A[left]
            index += 1
            left += 1
        while right <= end:
            self.tmp[index] = A[right]
            index += 1
            right += 1
        for left in range(start, end + 1):  # COPY BACK content FROM TMP to A
            A[left] = self.tmp[left]
        return cnt

    def merge_sort(self, A, start, end):
        if start >= end:
            return 0
        mid = (start + end) // 2
        # 先递归数两边 再于merge环节中数横跨左右的  横跨左右逆序对判断条件为 = A[left] > A[right]
        left_count = self.merge_sort(A, start, mid)
        right_count = self.merge_sort(A, mid + 1, end)
        total_count = self.merge_and_count(A, start, end, mid, left_count + right_count)
        return total_count

print(Solution().reversePairs([2,4,1,3,5]))
