

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """https://leetcode.cn/problems/set-matrix-zeroes/
        Do not return anything, modify matrix in-place instead.

        Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
        """
        if not matrix or not matrix[0]:
            return
        ROWS, COLS = len(matrix), len(matrix[0])
        first_row_zero = False
        # determine which row/col need to be zeroed
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  # 第一行用来标记每一列是否应该被清零, 0...COLS-1共COLS列
                    # skipping (0,0) avoid marking repeatedly & lose information
                    if r > 0:
                        # 第一列用来标记每一行是否应该被清零(除了第一行)
                        # 第一行应该被记在0,0 但我们在记录每列是否应该置零时已经占用了(0,0) (0,0)代表第一列是否应该被清零
                        # 所以需要额外O(1)储存记录此信息
                        matrix[r][0] = 0
                    elif r == 0:  # 使用额外O(1)储存记录第一行是否应该被清零
                        first_row_zero = True
        for r in range(1, ROWS):  # zeroed out 除去第一行第一列外内容
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:  # zeroed out the first column
            for r in range(ROWS):
                matrix[r][0] = 0
        if first_row_zero:  # zeroed out the first row
            for c in range(COLS):
                matrix[0][c] = 0
