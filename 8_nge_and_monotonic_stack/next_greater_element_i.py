from collections import deque


# https://leetcode.cn/problems/next-greater-element-i/description/
class Solution:
    # find next greater element for each element in nums1 in nums2 array
    # 1. traverse nums2 array backward,
    #         pop all elements <= curr element from stack
    #         stack top is next greater element of curr element (if stack is nonempty)
    #         record that in our results map (a map that maps each nums2 element to its next greater element (nge))
    # 2. since nums1 is a subarray of nums2, we can map nge array on nums2 to nge array on nums1 given result map
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = {}  # a map that maps element in nums2 to its next greater element if exist
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                result[nums2[i]] = stack[-1]
            else:
                result[nums2[i]] = -1
            stack.append(nums2[i])
        return [result[num] for num in nums1]
