from math import inf

class Solution:
    # total=6 half=total//2=3 (always shorter half)
    # nums1=[1,2,3,4] nums2=[1,2]
    # 想要left partition size为3
    # 先切一刀mid在短的数组上
    # amid = (l + r) // 2 = 0
    # bmid = half - i - 2  # -2 because total is 1 based, index for both array 0-based, off by 2
    # example: amid=0, bmid=1
    # [1 2][3 4]  
    # [1][2]
    # init al,bl,ar,br value based on amid bmid, handle edge case by float("inf") float("-inf")
    # 因为我们要交叉比较 对于越界情况取-inf, inf要根据我们
    # 要满足的核心二分查找条件 al <= br and bl <= ar判断
    # 左边越界则视作比较时永远小于右边 右边越界则视作比较时永远大于左边
    # 如果想要满足partition by half, we need  al <= br and bl <= ar
    # [...bl][br...]
    # [...al][ar...]
    # if this is satisfied, return median
    #    total is even: (max(al, bl) + min(ar, br)) / 2
    #    total is odd: return min(ar, br)
    # 不满足left partition 整体大于right partition的话 则需要调整a数组切一刀指针位置
    # 相当于在短的a数组中二分查找 找到后更新b数组切一刀指针位置
    # al > br or bl > ar
    # first case: a切的靠后 al太大要少切 r = amid - 1
    # second case:  b切的靠后 bl太大 a要多切点 l = amid + 1

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(b) < len(a):
            a, b = b, a
        # a is smaller array
        l, r = 0, len(a) - 1
        while True:
            amid = (l + r) // 2
            bmid = half - amid - 2
            al = a[amid] if amid >= 0 else float("-inf")
            ar = a[amid + 1] if amid + 1 < len(a) else float("inf")
            bl = b[bmid] if bmid >= 0 else float("-inf")
            br = b[bmid + 1] if bmid + 1 < len(b) else float("inf")
            if al <= br and bl <= ar:
                if total % 2 == 1:
                    return min(ar, br)
                else:
                    return (max(al, bl) + min(ar, br)) / 2
            elif al > br:
                r = amid - 1
            elif bl > ar:
                l = amid + 1
        

class Solution2:
    """ https://www.lintcode.com/problem/65/
    Description
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.
The overall run time complexity should be O(log(m + n))O(log(m+n)).

The definition of the median:

The median here is equivalent to the median in the mathematical definition.
The median is the middle of the sorted array.
If there are n numbers in the array and n is an odd number, the median is A[(n - 1) / 2]A[(n−1)/2].
If there are n numbers in the array and n is even, the median is A[(n - 1) / 2] + A[(n - 1) / 2 + 1]) /
2A[(n−1)/2]+A[(n−1)/2+1])/2.
For example, the median of the array A=[1,2,3] is 2, and the median of the array A=[1,19] is 10.
Example
Example 1:

Input:

A = [1,2,3,4,5,6]
B = [2,3,4,5]
Output:

3.5
Explanation:

The combined array is [1,2,2,3,3,4,4,5,5,6], and the median is (3 + 4) / 2.
Example 2:

Input:

A = [1,2,3]
B = [4,5]
Output:

3
Explanation:

The combined array is [1,2,3,4,5], and the median is 3.

Challenge
The overall run time complexity should be O(log (m+n))O(log(m+n)).

Tags
Binary Search
Related Problems
931
Median of K Sorted Arrays
Hard
81
Find Median from Data Stream
Hard
80
Median
Easy

        @param: A: An integer array
        @param: B: An integer array
        @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 小的在前
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        even_len = (x + y) % 2 == 0
        while low <= high:
            lx_len = int((low + high) / 2)
            ly_len = int((x + y + 1) / 2 - lx_len)
            lx_max = -inf if lx_len == 0 else nums1[lx_len - 1]
            ly_max = -inf if ly_len == 0 else nums2[ly_len - 1]
            rx_min = inf if lx_len == x else nums1[lx_len]
            ry_min = inf if ly_len == y else nums2[ly_len]
            # 交叉比较 确定是否达到invariant 左半<=右半
            if lx_max <= ry_min and ly_max <= rx_min:
                if even_len:
                    return (max(lx_max, ly_max) + min(rx_min, ry_min)) / 2
                else:
                    return max(lx_max, ly_max)
            # lx_max大了 去x的左半查找 否则 去x的右半查找
            elif lx_max > ry_min:
                high = lx_len - 1
            elif ly_max > rx_min:
                low = lx_len + 1
        return -1

