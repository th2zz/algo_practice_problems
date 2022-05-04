class Solution:
    # https://leetcode.cn/problems/spiral-matrix/
    # Given an m x n matrix, return all elements of the matrix in spiral order.
    """
    123
    456
    789      123698745

    ---|
    [  |
    ===|

[[1, 1, 1, 1, 1, 1, 1],
 [1, 2, 2, 2, 2, 2, 1],
 [1, 2, 3, 3, 3, 2, 1],
 [1, 2, 2, 2, 2, 2, 1],
 [1, 1, 1, 1, 1, 1, 1]]

    一层一层模拟 最上层 最右边 最下边 最左边 4指针边界缩圈
    Time O(mn) Space O(1)
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        n, m = len(matrix), len(matrix[0])
        res = []
        left, right, top, bottom = 0, m - 1, 0, n - 1
        while len(res) < n * m:
            for col in range(left, right + 1):  # top side
                if len(res) < n * m:
                    res.append(matrix[top][col])
            for row in range(top + 1, bottom + 1):  # rightmost side
                if len(res) < n * m:
                    res.append(matrix[row][right])
            for col in range(right - 1, left - 1, -1):  # bottom side
                if len(res) < n * m:
                    res.append(matrix[bottom][col])
            for row in range(bottom - 1, top, -1):  # leftmost side
                if len(res) < n * m:
                    res.append(matrix[row][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return res
