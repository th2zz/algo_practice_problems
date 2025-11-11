class Solution:
    # Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
    # nums = [4,3,2,7,8,2,3,1], output [5,6] nums = [1,1], output [2]
    # traverse input array,  
    #    put number into the corresponding bucket (index num - 1) and make it negative as a marker
    # finally loop through, if there are positive number, then i + 1 is original value that's missing
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in enumerate(nums):
            nums[abs(num) - 1] = abs(nums[abs(num) - 1]) * -1
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i + 1)
        return res
