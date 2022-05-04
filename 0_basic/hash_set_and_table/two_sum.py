class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  # input not sorted, return two sum indices
        if not nums:
            return []
        val2idx = {}
        for i, n in enumerate(nums):
            if target - n in val2idx:
                return [val2idx[target - n], i]
            val2idx[n] = i
        return [-1, -1]
