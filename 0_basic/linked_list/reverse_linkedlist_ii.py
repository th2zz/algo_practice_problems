# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:  # https://leetcode.cn/problems/reverse-linked-list-ii/?envType=study-plan-v2&envId=top-interview-150
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """

        从dummy开始找到要反转部分head前一个节点pre,走left-1步
        fixing cur = 2 pre = 1,
            insert cur.next before cur 头插法, repeat for right - left times: e.g. for 12345, left=2,right=4 3nodes list, repeat 2 times
            - save cur.next reference
            - let cur.next skip the node to be inserted at front
            - insert the node at front and update pre.next reference
        1->2->3->4->5
        left = 2  right = 4
        1 -> 2->3->4->5
        1 -> 2->4->5
        1 -> 3->2->4->5
        1 -> 3->2->5
        1 -> 4->3->2->5
        """
        # 设置 dummyNode 是这一类问题的一般做法
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next
        # 头插法
        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next
