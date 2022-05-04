class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            nums[abs(num) - 1] = abs(nums[abs(num) - 1]) * -1
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i + 1)
        return res
