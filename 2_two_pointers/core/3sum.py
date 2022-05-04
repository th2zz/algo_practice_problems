from typing import List


class Solution:  # https://leetcode.cn/problems/3sum/submissions/568518870/?envType=study-plan-v2&envId=top-interview-150
    # return 3sum to zero
    #  O(n^2 + NlogN) time overall O(k) space k=#solutions
    # 输入没有排好序 解考虑去重
    # 锚定/遍历三元组中的最小值 起始位置 去锚定点右边 找two sum = -锚定值 unique pair
    # 注意起点的锚定边界 last pos: len(nums) - 3
    # 去重 if i > 0 and nums[i] == nums[i - 1]: continue
    # nums[i] is first element in triple, find two sum数组起始位置为i + 1
    # 带有去重逻辑的two sum, target = -nums[i] (锚定的triplet中最小值), 存在解就加到results中
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        results = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.find_two_sum_unique_pairs_with_boundaries(
                start=i + 1,
                end=len(nums) - 1,
                nums=nums,
                target=-nums[i],
                results=results,
            )
        return results

    def find_two_sum_unique_pairs_with_boundaries(
        self,
        start: int,
        end: int,
        target: int,
        nums: List[int],
        results: List[int],
    ) -> None:
        # O(n)
        while start < end:
            sum = nums[start] + nums[end]
            if sum < target:
                start += 1
            elif sum > target:
                end -= 1
            else:
                results.append([-target, nums[start], nums[end]])
                start += 1
                end -= 1  # because input is sorted, we can dedup like this
                while start < end and start > 0 and nums[start] == nums[start - 1]:
                    start += 1
                while start < end and end < len(nums) and nums[end] == nums[end + 1]:
                    end -= 1

    def regular_two_sum_unique_pair(self, nums, target):
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        res = 0
        nums = sorted(nums)
        while (
            left < right
        ):  # 双指针解决2sum unique pair问题需要数据有序, 可以有重复(无所谓)
            two_sum = nums[left] + nums[right]
            if two_sum == target:
                res += 1
                right -= 1
                left += 1
                while left < right and nums[left] == nums[left - 1]:  # 去重
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif two_sum > target:
                right -= 1
            else:
                left += 1
