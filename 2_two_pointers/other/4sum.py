class Solution:
    """
    https://www.lintcode.com/problem/58/

find unique quadruplets a, b, c, d that sum to target.  Input is not sorted and can have duplicates

- O(n^3 + nlogn)  O(k) k=#solutions
  - 双层for循环固定两个点
  - 双指针扫描后续数组 find two sum unique pairs
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        pass
