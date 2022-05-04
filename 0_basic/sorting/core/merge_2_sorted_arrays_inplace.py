class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """https://leetcode.cn/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
        nums1 size m + n, nums1 m elements, nums2 n elements
        merge 2 sorted array in place
        """
        k = m + n - 1
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        while i >= 0:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
