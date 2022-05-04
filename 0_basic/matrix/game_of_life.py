from typing import List


class Solution:  # https://leetcode.cn/problems/game-of-life/?envType=study-plan-v2&envId=top-interview-150
    def _inside(self, board: List[List[int]], x: int, y: int) -> bool:
        return 0 <= x < len(board) and 0 <= y < len(board[0])

    # spiral matrix 环绕式遍历一圈
    def count_neighbors(self, board, r, c):
        nei = 0
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                # 起点或越界 跳过
                if (i == r and j == c) or not self._inside(board, i, j):
                    continue
                # originally a 1 (before or after modified)
                if board[i][j] in [1, 8, 9]:
                    nei += 1
        return nei

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Modify and set next state of the board
        Do not return anything, modify board in-place instead.
        """
        """
        live cell:
          - with 2 or 3 live neighbors: live to next generation
          - otherwise dies
        dead cell: 
          - exactly 3 live neighbors become alive
        Encode Cell state:
        Original | New | State
           0     | 0   |  0
           0     | 1   |  7
           1     | 0   |  8
           1     | 1   |  9
        """
        rows, cols = len(board), len(board[0])
        # count neighbor and encode state of each pos in-place
        for r in range(rows):
            for c in range(cols):
                nei = self.count_neighbors(board, r, c)
                if board[r][c] == 1 and nei in [2, 3]:
                    board[r][c] = 9
                if board[r][c] == 1 and (nei < 2 or nei > 3):
                    board[r][c] = 8
                elif board[r][c] == 0 and nei == 3:
                    board[r][c] = 7
        # recover new global state from encoded state
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 8:
                    board[r][c] = 0
                if board[r][c] in [7, 9]:
                    board[r][c] = 1


arr = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]

Solution().gameOfLife(arr)
print(arr)
expected = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
print(expected)
