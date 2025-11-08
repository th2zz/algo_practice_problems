from itertools import accumulate
from typing import List


class NumArray:
    # Initializes the object with the integer array nums.
    # s = [0] * (len(nums) + 1)
    # for i, x in enumerate(nums):
    #     s[i + 1] = s[i] + x
    def __init__(self, nums: List[int]):
        s = list(accumulate(nums, initial=0))  # a good way to prepare prefix sum array [0, 1, 3, ..]
        self.s = s

    # Returns the sum of the elements of nums between indices left and right inclusive
    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# [-2, 0, 3, -5, 2, -1]

# [2, 5]
# s[i] = sum of first i elements
# s[0] = 0
# s[1] = -2
# s[2] = -2
# s[3] = 1
# s[4] = -4
# s[5] = -2
# s[6] = -3
# sumRange(left=2, right=5) = s[6] - s[2] = -3 - -2 = -1
# s[4] = e1 + e2 + e3 + e4
# s[2] = e1 + e2
# sumRange(2,3) = sum of elements from index 2 to 3 = e3 + e4 = s[4] - s[2]
# sumRange(l, r) = s[r + 1] - s[l] s

# >>> from itertools import accumulate
# >>> s = list(accumulate([1,2,3], initial=0))
# >>> s
# [0, 1, 3, 6]
