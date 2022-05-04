class Solution:
    """https://www.lintcode.com/problem/1343/?_from=collection&fromId=161
    Description
Given you two strings which are only contain digit character. You need to return a string spliced by the sum of the bits.
A and B are strings which are composed of numbers

Example
Example1:
Input:
A = "99"
B = "111"
Output: "11010"
Explanation: because 9 + 1 = 10, 9 + 1 = 10, 0 + 1 = 1,connect them，so answer is "11010"

Example2:
Input:
A = "2"
B = "321"
Output: "323"
Explanation: because 2 + 1 = 3, 2 + 0 = 2, 3 + 0 = 3, connect them，so answer is "323"

Tags
String
Simulation
Company
Quora
    @param A: a string
    @param B: a string
    @return: return the concatenated sum of two strings digit by digit (not like regular add operation with overflow)
    """

    def SumofTwoStrings(self, A, B):
        if not A and not B:
            return ''
        if not A:
            return B
        if not B:
            return A
        i, j = len(A) - 1, len(B) - 1
        res = ''
        while i >= 0 and j >= 0:  # similar to merge two sorted array subroutine in merge sort
            res = str(int(A[i]) + int(B[j])) + res  # fill res from right to left
            i -= 1
            j -= 1
        if i >= 0:
            res = A[:i + 1] + res  # insert remaining [...i] to the front
        elif j >= 0:
            res = B[:j + 1] + res  # insert remaining [...j] to the front
        return res

# print(Solution().SumofTwoStrings("99", "111"))
# print(Solution().SumofTwoStrings("2", "321"))
