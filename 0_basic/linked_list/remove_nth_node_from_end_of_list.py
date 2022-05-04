# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        p1 = dummy  # p1往前放一个位置开始 而不是在head上 这样退出while p2循环时 p1.next为要删的节点
        p2 = head
        for i in range(n):  # assume n is always in range no need to check if p2 is none
            p2 = p2.next
        while p2:
            p2 = p2.next
            p1 = p1.next
        # node_to_be_deleted = p1.next
        p1.next = p1.next.next
        # node_to_be_deleted.next = None
        return dummy.next
