from collections import deque
# https://leetcode.cn/problems/next-greater-element-i/description/
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = deque()
        result = {}
        # find next greater element array for nums2 array
        for i in range(len(nums2) - 1, -1, -1):
            # while stack nonempty and stack top <= current element
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                result[nums2[i]] = stack[-1]
            else:
                result[nums2[i]] = -1
            stack.append(nums2[i])
        return [result[num] for num in nums1]
