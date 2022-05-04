# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:  # https://leetcode.cn/problems/reverse-linked-list-ii/?envType=study-plan-v2&envId=top-interview-150
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """

        从dummy开始找到要反转部分head前一个节点pre,走left-1步
        fixing fixed_head = 2 pre = 1,
            insert fixed_head.next before fixed_head 头插法, repeat for right - left times: e.g. for 12345, left=2,right=4 3nodes list, repeat 2 times
            - save fixed_head.next reference
            - let fixed_head.next skip the node to be inserted at front
            - insert the node at front and update pre.next reference
        left = 2  right = 4 fixed_head=2 pre=1 next=3
        1 -> 2->3->4->5   fixed_head.next=4 (2->4) next.next=pre.next (3->2) pre.next=next 1->3->2->4
        1 -> 3->2->4->5   now next is 4, move 4 to front
        1 -> 4->3->2->5
        """
        # 设置 dummyNode 是这一类问题的一般做法
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next
        # 头插法, insert nodes before fixed head
        fixed_head = pre.next
        for _ in range(right - left):
            next = fixed_head.next
            fixed_head.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next
