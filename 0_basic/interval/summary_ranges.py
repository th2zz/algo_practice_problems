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
            i += 1
        return res
