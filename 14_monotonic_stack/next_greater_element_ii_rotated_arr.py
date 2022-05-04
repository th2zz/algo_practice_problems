from typing import List


class Solution:
    # https://leetcode.cn/problems/next-greater-element-ii/description/
    # find nge arr of a circular array (next element of last element is nums[0])
    # we do an iteration backward from index 2n-1
    #    each current element is accessed as nums[i % n]
    #    so essentially we traverse original array 2 times [arr][arr_copy] and only fill in result at last pass
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [-1] * n
        for i in range(2 * n - 1, -1, -1):
            x = nums[i % n]
            while stack and stack[-1] <= x:
                stack.pop()
            if stack and i < n:
                res[i] = stack[-1]
            stack.append(x)
            print(stack, res)
        return res


sol = Solution()
assert sol.nextGreaterElements(nums=[1, 2, 1]) == [2, -1, 2]
print("---")
assert sol.nextGreaterElements(nums=[1, 2, 3, 4, 3]) == [2, 3, 4, -1, 4]
