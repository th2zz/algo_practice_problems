class Solution:
    """https://www.lintcode.com/problem/547/
    Description
Given two arrays, write a function to compute their intersection.

Each element in the result must be unique.
Example
Example 1:

Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2],
Output: [2].
Example 2:

Input: nums1 = [1, 2], nums2 = [2],
Output: [2].
Challenge
Can you implement it in three different algorithms?

Tags
Same Direction Two Pointers
Hash Table
Binary Search

Company
Facebook
Uber
Related Problems
548
Intersection of Two Arrays II
Easy
248
Count of Smaller Number
Medium

    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """

    # same direction two pointers; like merge two sorted arrays but not merging: only add to intersection set if equal
    def intersection(self, nums1, nums2):
        nums1.sort()  # inplace sort
        nums2.sort()  # O(nlogn+mlogm) for sort, O(m+n) for finding intersection, O(1) space
        i, j = 0, 0
        intersection = set()
        while i < len(nums1) and j < len(nums2):  # consider relationship of i, j in sorted nums1, nums2 resp.
            if nums1[i] < nums2[j]:  # 哪边小哪边指针前进
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                intersection.add(nums1[i])
                i += 1
                j += 1
        return list(intersection)

    # https://realpython.com/binary-search-python/#using-the-bisect-module
    # binary search with built-in library O(mlogm + nlogm) O(1)
    # 遍历数组2每个元素 二分搜索元素在数组1中位置 如果没越界且相等 则加到交集中
    def intersection0(self, nums1, nums2):
        nums1.sort()
        res = set()
        import bisect
        for n in nums2:  # find element n index i in nums1 s.t.
            index = bisect.bisect_left(nums1, n)  # [nums1[lo:i]: <n] [nums1[i:hi]: >=n]
            if index in range(len(nums1)) and nums1[index] == n:
                res.add(nums1[index])
        return list(res)

    def binarySearch(self, nums, target):  # find first position of target, can have duplicates
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        return -1

    # binary search: self written subroutine find first pos of target (duplicates allowed) O(mlogm + nlogm) O(1)
    def intersection0_(self, nums1, nums2):
        nums1.sort()
        res = set()
        for n in nums2:  # find element n index i in nums1 s.t.
            index = self.binarySearch(nums1, n)  # [nums1[lo:i]: <n] [nums1[i:hi]: >=n]
            if index in range(len(nums1)) and nums1[index] == n:
                res.add(nums1[index])
        return list(res)

    # use & or by use list comprehension by definition
    def intersection1(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

    def intersection1_(self, nums1, nums2):
        s1, s2 = set(nums1), set(nums2)
        return [x for x in s1 if x in s2]

    # hashtable, O(m+n) O(max(m,n))
    def intersection2(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set()
        for num in nums2:
            if num in s1:
                s2.add(num)
        return list(s2)
