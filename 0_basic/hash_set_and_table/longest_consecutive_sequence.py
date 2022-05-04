class Solution:  # https://leetcode.cn/problems/longest-consecutive-sequence/
    # input unsorted, return length of the longest consecutive sequence in O(n)
    """
        Example 1:

    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
    Example 2:

    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9

    Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        unused = set(nums)  # 用nums初始化一个set 记录未使用的数
        res = 0
        for item in nums:  # 枚举中心点值
            # 未使用 则 向(值)两侧扩散 找最长连续序列 并将沿途数从unused删除 打擂台记录最大长度
            if item in unused:
                unused.remove(item)
                l, r = item - 1, item + 1
                while l in unused:
                    unused.remove(l)
                    l -= 1
                while r in unused:
                    unused.remove(r)
                    r += 1
                res = max(res, r - l - 1)
        return res

    def longestConsecutive2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dedup_nums = set(nums)
        longest_len = -1
        for num in nums:
            # enumerate consecutive sequence starts 没有比他小的数=start
            if num - 1 not in dedup_nums:
                streak = 1
                curr = num
                while curr + 1 in dedup_nums:
                    curr += 1
                    streak += 1
                # 利用set数consecutive sequence with this start的长度 打擂台记录最大值
                longest_len = max(longest_len, streak)
        return longest_len
