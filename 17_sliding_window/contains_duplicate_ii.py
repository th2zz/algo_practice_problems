class Solution:
    # https://leetcode.cn/problems/contains-duplicate-ii/solutions/1218075/cun-zai-zhong-fu-yuan-su-ii-by-leetcode-kluvk/?envType=study-plan-v2&envId=top-interview-150
    # Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
    # Example 1:
    # Input: target = 7, nums = [2,3,1,2,4,3]
    # Output: 2
    # Explanation: The subarray [4,3] has the minimal length under the problem constraint.
    # Example 2:
    # Input: target = 4, nums = [1,4,4]
    # Output: 1
    # Example 3:
    # Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    # Output: 0
    # abs(i - j) <= k offset difference is k, this window has k + 1 elements and there are duplicate number in window
    # window size k + 1
    # k+1 first index out of window 在哪停取决于我们要做什么操作
    # slidingwindow maxium我们要在window最后一个元素位置结算当前maximum
    # 而这里我们只是在out of window第一个位置删掉window起始元素
    # i - windowsize: index of element out of window, in this problem it's i - (k + 1)
    # i - windowsize + 1: index of first element in window
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        window = set()
        for i in range(n):
            if i >= k + 1:
                window.remove(nums[i - k - 1])
            if nums[i] in window:
                return True
            window.add(nums[i])
        return False
