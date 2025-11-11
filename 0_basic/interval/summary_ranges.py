"""
给定一个  无重复元素 的 有序 整数数组 nums 。

区间 [a,b] 是从 a 到 b（包含）的所有整数的集合。

返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个区间但不属于 nums 的数字 x 。

列表中的每个区间范围 [a,b] 应该按如下格式输出：

"a->b" ，如果 a != b
"a" ，如果 a == b
 

示例 1：

输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
示例 2：

输入：nums = [0,2,3,4,6,8,9]
输出：["0","2->4","6","8->9"]
解释：区间范围是：
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
"""
class Solution:  # https://leetcode.cn/problems/summary-ranges/submissions/567200377/?envType=study-plan-v2&envId=top-interview-150
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i, n = 0, len(nums)
        res = []
        while i < n:
            start = i  # 锚定start i右边走跳过连续的数 注意边界判断
            while i + 1 < n and nums[i] + 1 == nums[i + 1]:
                i += 1
            # 判断当前区间start...i是否构成一组解 注意边界判断
            temp = str(nums[start])
            if start < i:
                temp += "->" + str(nums[i])
            res.append(temp)
            i += 1  # try a new start
        return res
