# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.cn/problems/reorder-list/
class Solution:  # O(N) O(1) N=#list nodes
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        reorder linkedlist s.t.

        L0 → L1 → … → Ln - 1 → Ln      becomes
        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

        Input: head = [1,2,3,4]
        Output: [1,4,2,3]

        Input: head = [1,2,3,4,5]
        Output: [1,5,2,4,3]

        lists are not guranteed to be sorted
        """
        if not head:
            return
        mid = self.firstHalfEnd(head)  # 快慢指针找到链表中点 l2在奇数长度下指向较短那个
        l1 = head  # 取出两个链表 断开他们 by mid.next=None
        l2 = mid.next  # odd长度下 l1为较长的那个 l2为较短的  even length= normal
        mid.next = None
        l2 = self.reverse(l2)  # reverse l2后合并(interleave)到l1里
        self.interleave(l1, l2)

    # https://leetcode-cn.com/problems/middle-of-the-linked-list/
    # 和这道题区别在于 偶数长度下需要返回偏左的中点
    def firstHalfEnd(self, head: ListNode) -> ListNode:  # find midpoint with slow & fast ptr
        slow = fast = head
        while fast.next and fast.next.next:  # 1234=>2 12345=>3
            slow = slow.next
            fast = fast.next.next
        return slow

    # normal reverse linkedlist
    def reverse(self, head):
        prev, cur = None, head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    # interleave l2 into l1, special case of merge 2 linkedlists
    def interleave(self, l1, l2):
        while l1 and l2:
            l1_remains, l2_remains = l1.next, l2.next
            l1.next, l2.next = l2,  l1_remains
            l1, l2 = l1_remains, l2_remains
