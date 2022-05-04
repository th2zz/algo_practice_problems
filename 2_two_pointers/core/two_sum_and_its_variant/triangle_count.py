class Solution:
    """
    382 · Triangle Count
    Algorithms
    Medium
    Accepted Rate
    41%

    Description
    Given an array of integers, how many three numbers can be found in the array, so that we can build an triangle 
    whose three edges length is the three numbers that we find?

    Example
    Example 1:

    Input: [3, 4, 6, 7]
    Output: 3
    Explanation:
    They are (3, 4, 6),
             (3, 6, 7),
             (4, 6, 7)
    Example 2:

    Input: [4, 4, 4, 4]
    Output: 4
    Explanation:
    Any three numbers can form a triangle.
    So the answer is C(3, 4) = 4
    @param S: A list of integers
    @return: An integer
    """

    def triangle_count(self, s) -> int:
        if not s:
            return 0
        res = 0
        s.sort()  # TODO 必须的因为我们要复用双指针求two sum的解
        for i in range(2, len(s)):  # 遍历最大边索引位置[2...len(s)-1] 最大边左边[0...i-1]寻找两个小边 two_sum > target
            res += self.two_sum_gt(s, 0, i - 1, s[i])
        return res

    def two_sum_gt(self, s, left, right, target):
        """
        找到target_index 左边  两数之和 > target_sum的组合的个数
        """
        res = 0
        while left < right:
            sum = s[left] + s[right]
            if sum <= target:
                left += 1
            else:
                res += right - left  # add in batch
                right -= 1
        return res