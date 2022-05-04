class Solution:
    """
    https://www.lintcode.com/problem/976/

    给了4个数组 每组里选1个数 使得4sum to 0, find #solutions
    # 本题类似two sum iii data structure design
    #  维护一个 ab和:频次 的map   4sum to 0 needs a + b = -(c + d)
    #  双重循环遍历cd 累加-(c+d)出现次数 = 4sum to 0的解个数
    - input not sorted
    - input has duplicates
    - no need to eliminate duplicate answer
    @param A: a list
    @param B: a list
    @param C: a list
    @param D: a list
    @return: how many tuples (i, j, k, l) there are s.t. A[i] + B[j] + C[k] + D[l] is zero
    """

    def fourSumCount(self, A, B, C, D):
        table = {}
        for a in A:
            for b in B:
                table[a + b] = table.get(a + b, 0) + 1
        cnt = 0
        for c in C:
            for d in D:
                cnt += table.get(-(c + d), 0)
        return cnt
