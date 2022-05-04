class Solution:
    def swap(self, arr, i, j):
        # swap element at i, j in arr
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def rotate(self, matrix: List[List[int]]) -> None:
        """ https://leetcode.cn/problems/rotate-image/
        Do not return anything, modify matrix in-place instead.
        given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

        You have to rotate the image in-place
        Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        Output: [[7,4,1],[8,5,2],[9,6,3]]

        Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

        Constraints:
            n == matrix.length == matrix[i].length
            1 <= n <= 20
            -1000 <= matrix[i][j] <= 1000


        # transpose a matrix: flip by diagonal, row become col, col become row
        123              147                      741
        456              258                      852
        789  transpose=> 369  horizontal mirror=> 963
        rotate clockwise 90 degrees <=> take a transpose, mirror horizontally
        rotate counterclockwise 90 degrees <=> take a transpose, mirror vertically
        """
        if not matrix or not matrix[0]:
            return
        n = len(matrix)  # Time O(mn) Space O(1)
        for i in range(n):  # flip by diagonal  top-left to bottom-right
            for j in range(i, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(n):  # mirror horizontally
            for j in range(n//2):
                self.swap(matrix[i], j, n - j - 1)
