class Solution:
    # https://leetcode.cn/problems/next-greater-element-ii/description/
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = deque()
        n = len(nums)
        res = [-1] * n
        for i in range(2*n - 1, -1, -1):
            x = nums[i % n]
            while stack and stack[-1] <= x:
                stack.pop()
            if stack and i < n:
                res[i] = stack[-1]
            stack.append(x)
        return res