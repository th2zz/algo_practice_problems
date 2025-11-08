from collections import deque

# https://leetcode.cn/problems/sliding-window-maximum/description/
class MonotonicQueue:
    def __init__(self) -> None:
        self.data = deque()

    def push(self, item: int) -> None:
        # remove items from end of the queue if they are smaller than item
        while self.data and self.data[-1] < item:
            self.data.pop()
        self.data.append(item)

    def max(self) -> int:
        return self.data[0]

    def pop(self) -> None:
        self.data.popleft()

    def empty(self) -> bool:
        return len(self.data) == 0

    def peek(self) -> int:
        return self.max()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = MonotonicQueue()
        res = []
        for i in range(len(nums)):
            if i < k - 1:
                # append first k-1 items to window
                window.push(nums[i])
            else:
                window.push(nums[i])
                res.append(window.max())
                window_start = nums[i - k + 1]
                if not window.empty() and window.max() == window_start:
                    window.pop()
        return res


# [1,3,-1,-3,5,3,6,7] 3

# [1]  1
