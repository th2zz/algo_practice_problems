class Solution:
    """sort an integer array with merge sort
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers2(self, A):
        if not A:
            return A
        temp = [0] * len(A)
        self.merge_sort(A, 0, len(A) - 1, temp)

    def merge_sort(self, A, start, end, temp):
        if start >= end:
            return
        mid = (start + end) // 2
        self.merge_sort(A, start, mid, temp)
        self.merge_sort(A, mid + 1, end, temp)
        self.merge(A, start, end, temp)

    def merge(self, A, start, end, temp):  # O(NlogN) O(N) stable
        # merge left, right half, fill results to temp, write temp back to A[start:end]
        mid = (start + end) // 2
        left = start
        right = mid + 1
        index = start
        while left <= mid and right <= end:
            if A[left] < A[right]:
                temp[index] = A[left]
                index += 1
                left += 1
            else:
                temp[index] = A[right]
                index += 1
                right += 1
        while left <= mid:
            temp[index] = A[left]
            index += 1
            left += 1
        while right <= end:
            temp[index] = A[right]
            index += 1
            right += 1
        for i in range(start, end + 1):
            A[i] = temp[i]
#
#
# a = [3,2,1,4,5]
# Solution().sortIntegers2(a)
# print(a)
