class Solution:
    # https://leetcode.cn/problems/find-the-duplicate-number/?envType=company&envId=google&favoriteSlug=google-six-months
    # 将数组下标访问视作链表.next操作 则可将此问题转化为 快慢指针判断链表是否有环的问题
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            # fast 前进两次，slow 前进一次
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        # ptr == slow 时说明检测到重复元素，两个重复元素同时指向环的入口。
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
