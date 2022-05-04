# https://leetcode-cn.com/problems/contains-duplicate/
class Solution:
    # return if there is dup in nums
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        visited = set()
        for n in nums:
            if n in visited:
                return True
            visited.add(n)
        return False
