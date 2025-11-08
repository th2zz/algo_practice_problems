from typing import List


class Solution:
    """https://www.lintcode.com/problem/654/
    2维矩阵初始化 C = [[0] * l for _ in range(n)]  for _ deep copy list 避免 list只有引用被copy
    暴力法 C[i][j] = A row i dot B col j
        time: worst case O(n * l * m) assume square matrix O(n^3) cubic time
        space: O(1) extra space
    三重循环 n m l 累加C[i][k] += A[i][j] * B[j][k] 跳过A中空元素
        same
    2 pass hashtable store nonzero elements then traverse and add partial product C[i][k] += A[i][j] * B[j][k]:
        time: O(n * m) + O(n * k * l) assume square matrix n = m = l  O(n^2) + O(k * n^2) ~ O(kn^2)
        space: O(n * m) ~ O(n^2) if assuming square matrix
    same as above but only store nonzero elements index with hashtable
        time: same O(kn^2)
        space O(n^2) but less
    Given two Sparse Matrix A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example
Example1

Input:
[[1,0,0],[-1,0,3]]
[[7,0,0],[0,0,0],[0,0,1]]
Output:
[[7,0,0],[-7,0,3]]
Explanation:
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
Example2

Input:
[[1,0],[0,1]]
[[0,1],[1,0]]
Output:
[[0,1],[1,0]]
Tags
Mathmatics
Company
Facebook
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """

    def dot(self, v1, v2):
        """ Dot product of two vectors (each represented as list)
        employee_numbers = [2, 9, 18, 28]
        employee_names = ["Candice", "Ava", "Andrew", "Lucas"]
        zip results in an iterator of the following
        [('Candice', 2), ('Ava', 9), ('Andrew', 18), ('Lucas', 28)]
        """
        if len(v1) != len(v2):
            raise Exception("length mismatch")
        return sum(t[0] * t[1] for t in zip(v1, v2))

    def column(self, matrix, i: int):
        """
        extract ith column from a 2D matrix
        """
        # https://stackoverflow.com/questions/903853/how-do-you-extract-a-column-from-a-multi-dimensional-array
        return [row[i] for row in matrix]

    """  
    brute force matrix multiplication
    # https://stackoverflow.com/questions/6502575/python-call-by-reference-on-primitive-types
    # https://stackoverflow.com/questions/2739552/2d-list-has-weird-behavor-when-trying-to-modify-a-single-value
    # In python every variable is an object, and so a reference. Primitives are immutable;
    # https://www.cnblogs.com/ljxh/p/11286748.html
    # https://medium.com/@lokeshsharma596/is-python-call-by-value-or-call-by-reference-2dd7db74dbd0
    # https://stackoverflow.com/questions/8184244/i-thought-python-passed-everything-by-reference
    # http://dokelung.me/category/python/python-evaluation-strategy/
    # 2 3 3
    # [[1,0,0],
    #  [-1,0,3]]    2x3

    # [[7,0,0],     3x3
    #  [0,0,0],
    #  [0,0,1]]

    # [[7, 0, 0],   2x3   Cij = Arowi · Bcolj = sum(t[0] * t[1] for t in zip(L1, L2))
    #  [-7, 0, 3]]
    # time: worst case O(n * l * m) assume square matrix O(n^3) cubic time
    # space: O(1) extra space
    """


    def multiply0(self, A, B):  # complexity is the same as above
        if not A or not B or len(A[0]) == 0 or len(B[0]) == 0 or len(A[0]) != len(B):
            return None
        n = len(A)  # #rows A
        m = len(A[0])  # #cols A == rows B
        l = len(B[0])  # cols B
        C = [[0] * l for _ in range(n)]  # n x l matrix
        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:  # traverse each nonempty A position  (to speed up sparse matrix access)
                    continue
                for k in range(l):  # traverse result matrix 's columns because it's n by l
                    # C[i][k] = self.dot(A[i], self.column(B, k))  # dot product of A's ith row and B's kth col
                    # optimization: just sum up C[i][k] partial product while looping each j
                    C[i][k] += A[i][j] * B[j][k]
        return C

    def multiply1(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        # alternatively, we can use hashtable to store sparse matrix
        # let k = # non-zero elements in A;
        # O(n * m) + O(n * k * l) assume square matrix n = m = l  O(n^2) + O(k * n^2)
        # time complexity is about O(k * n^2)
        # extra space: O(n * m) ~ O(n^2) if assuming square matrix
        if not a or not b:
            return []
        n = len(a)  # #rows
        m = len(b)
        l = len(b[0])
        c = [[0] * l for _ in range(n)]
        # for i in range(n):
        #     for k in range(l):
        #         c[i][k] = self.dot(a[i], [row[k] for row in b])
        #
        #  final all nonzero elements in A, store them in nested dict s.t.  non_zeros_in_a[i][j] = a[i][j] && a[i][j] != 0
        non_zeros_in_a = {}  # k nonzero elements O(k)
        for i in range(n):
            non_zeros_in_ith_row = {}
            for j in range(m):
                if a[i][j] != 0:
                    non_zeros_in_ith_row[j] = a[i][j]
            non_zeros_in_a[i] = non_zeros_in_ith_row

        for i in range(n):
            ith_row_nz = non_zeros_in_a[i]  # traverse non-zero element
            for j, aij in ith_row_nz.items():  # for each non empty A[i][j]    (val = A[i][j])
                for k in range(l):  # add partial product to overall dot product at each C[i][k] = dot(ai bk)
                    c[i][k] += aij * b[j][k]  # vector ai dimension=j (m cols), vector bk dimension = j (m rows)  只有这些j才是非0的有意义的 才加
                    # 想象一下 两个vector点乘 v1中0位可以直接无视 （0，1，2） * （2，3，4） = 0*2 + 1*3 + 2*4 只有非0位才有贡献
        return c

    def multiply(self, a, b):  # 上面做法的问题在于其实没有必要存actual value, 只存a中非0元素在matrix中索引即可
        # OPTIMAL SOLUTION, time: same as above O(k * n^2)
        # space: O(n^2) but less space because not storing vals and only indices
        n = len(a)
        m = len(a[0])
        l = len(b[0])
        c = [[0] * l for _ in range(n)]
        nonzero_elements = {}  # i: set(ith row non zero elements col index)
        # find all nonzero elements in A, store these as index {i: set of column index at row i, ...}
        for i in range(n):
            ith_row_nz_idx = set()
            for j in range(m):
                if a[i][j] != 0:
                    ith_row_nz_idx.add(j)
            nonzero_elements[i] = ith_row_nz_idx
        for i in range(n):  # compute matrix multiplication
            for j in nonzero_elements[i]:  # for each non empty A[i][j]    (val = A[i][j])
                for k in range(l):  # add partial product to overall dot product at each c[i][k]
                    c[i][k] += a[i][j] * b[j][k]  # c[i][k] = a的i行 dot b的k列
        return c
# print(Solution().multiply([[1, 0, 0], [-1, 0, 3]], [[7, 0, 0], [0, 0, 0], [0, 0, 1]]))
# print(Solution().multiply(
# [[1,0,0],
#  [-1,0,3]],
#
# [[7,0,0],
#  [0,20,0],
#  [11,0,1]]
# ))

"""
[[1,0,0],
 [-1,0,3]]
 
[[7,0,0],
 [0,20,0],
 [11,0,1]]

[[7,0,11],[-7,0,-8]]

[[7,0,0],[26,0,3]]

"""
