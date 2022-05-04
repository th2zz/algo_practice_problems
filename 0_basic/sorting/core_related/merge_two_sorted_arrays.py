class Solution:
    """https://www.lintcode.com/problem/6/
    Description
Merge two given sorted ascending integer array A and B into a new sorted integer array.

Example
Example 1:

Input:

A = [1]
B = [1]
Output:

[1,1]
Explanation:

return array merged.

Example 2:

Input:

A = [1,2,3,4]
B = [2,4,5,6]
Output:

[1,2,2,3,4,4,5,6]
Challenge
How can you optimize your algorithm if one array is very large and the other is very small?

Tags
Related Problems
839
Merge Two Sorted Interval Lists
Easy
165
Merge Two Sorted Lists
Easy
64
Merge Sorted Array (easy version)
Easy

    """
    """ extra space O(n) merge two separated array
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, A, B):  # same one in merge sort
        i, j, n, m = 0, 0, len(A) - 1, len(B) - 1
        res = []
        while i <= n and j <= m:
            if A[i] < B[j]:
                res.append(A[i])
                i += 1
            elif A[i] >= B[j]:
                res.append(B[j])
                j += 1
        if i <= n:
            res.extend(A[i:])
        if j <= m:
            res.extend(B[j:])
        return res
