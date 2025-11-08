from typing import List


class Solution:
    # https://leetcode.cn/problems/daily-temperatures/description/
    # next greater element index difference
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []  # monotonic stack for storing next greater element index
        for i in range(len(temperatures) - 1, -1, -1):
            x = temperatures[i]
            while st and temperatures[st[-1]] <= x:
                st.pop()
            if st:
                res[i] = st[-1] - i
            st.append(i)
        return res

    # Given an array arr[] of integers, the task is to find the Next Greater Element for each element of the array in order of their appearance in the array.
    def next_greater_element(
        self,
        arr: list[int],
    ) -> list[int]:
        # naive approach takes O(n^2) O(1)
        # monotonic stack O(n) O(n)
        n = len(arr)
        res = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(arr[i])
        return res


# Input: arr[] = [1, 3, 2, 4]
# Output: [3, 4, 4, -1]
# Explanation: The next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4, since it doesn’t exist, it is -1.


# Input: arr[] = [6, 8, 0, 1, 3]
# Output: [8, -1, 1, 3, -1]
# Explanation: The next larger element to 6 is 8, for 8 there is no larger elements hence it is -1, for 0 it is 1 , for 1 it is 3 and then for 3 there is no larger element on right and hence -1.


# Input: arr[] = [10, 20, 30, 50]
# Output: [20, 30, 50, -1]
# Explanation: For a sorted array, the next element is next greater element also exxept for the last element.
sol = Solution()
assert sol.next_greater_element(arr=[1, 3, 2, 4]) == [3, 4, 4, -1]
assert sol.next_greater_element(arr=[6, 8, 0, 1, 3]) == [8, -1, 1, 3, -1]
assert sol.next_greater_element(arr=[10, 20, 30, 50]) == [20, 30, 50, -1]
print("passed")

sol = Solution()
assert sol.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]) == [
    1,
    1,
    4,
    2,
    1,
    1,
    0,
    0,
]
assert sol.dailyTemperatures(temperatures=[30, 40, 50, 60]) == [1, 1, 1, 0]
assert sol.dailyTemperatures(temperatures=[30, 60, 90]) == [1, 1, 0]
print("passed")
