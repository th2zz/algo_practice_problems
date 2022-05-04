class Solution:
    """https://www.lintcode.com/problem/138/?_from=collection&fromId=161
    EASY
Given an integer array, find a subarray where the sum of numbers is zero.
Your code should return the index of the first number and the index of the last number.

There is at least one subarray that it's sum equals to zero.

Example
Example 1:

Input:  [-3, 1, 2, -3, 4]
Output: [0, 2] or [1, 3].
Explanation: return anyone that the sum is 0.
Example 2:

Input:  [-3, 1, -4, 2, -3, 4]
Output: [1,5]
Tags
Hash Table
Prefix Sum Array
Array

Related Problems
405
Submatrix Sum
Medium
404
Subarray Sum II
Medium
406
Minimum Size Subarray Sum
Medium
139
Subarray Sum Closest
Medium

    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number that sums to 0
    给定一个数组 找到满足和为0的连续子数组 返回开始结束index 假设一定有解
本体可以通过前缀和的思想 + hashmap轻松解决
维系一个 {nums[:i +1]前缀和: i} 的字典 (每计算一个前缀和都加到字典中)  i是前缀和结束位置
遍历数组nums:
    计算当前前缀和
    如果当前前缀和见过 则返回[d[prefix_sum] + 1, i]
    添加当前 前缀和: i 映射关系到map中
找不到return [-1,-1]
    """

    # maintain a {prefix_sum_up_to_i (inclusive) : i} mapping
    # at pos i, prefix a + ... + b already seen
    # a + ... + b + c + ... + nums[i] = a + ... + b  <=>  c + ... + nums[i] = 0
    # then we return [index of c, i]     index of c = d[prefix_sum] + 1
    def subarraySum(self, nums):  # d存放 前缀和: 前缀和结束index
        d = {0: -1}  # TODO d[prefix_sum] + 1至少为0 需要初始化 0: value为-1; d[i]以i为prefix sum的最后一组解 结束index
        prefix_sum = 0  # prefix sum -> end_idx
        for i, num in enumerate(nums):
            prefix_sum += num  # 计算当前前缀和
            if prefix_sum in d:  # 如果见过当前前缀和 那么  [d[prefix_sum] + 1, ..., i] 为一组解
                return [d[prefix_sum] + 1, i]
            d[prefix_sum] = i  # 更新当前 前缀和:end_idx 映射关系到字典中 字典中仅维护了一组most up to date数据
        return [-1, -1]

nums = [-3, 1, 2, -3, 4]
print(Solution().subarraySum(nums))
nums = [-3, 1, -4, 2, -3, 4]
print(Solution().subarraySum(nums))
