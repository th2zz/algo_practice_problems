class Solution:
    """https://leetcode.cn/problems/remove-duplicates-from-sorted-array/submissions/569762189/?envType=study-plan-v2&envId=top-interview-150

    @param nums: an array of integers
    @return: the number of unique integers
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
