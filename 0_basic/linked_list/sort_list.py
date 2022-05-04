class Solution:
    def cut(self, head: ListNode) -> ListNode:  # 偶 返回右半开始 奇 返回右半开始(左3右2)
        # cut the LinkedList at the mid index with slow, fast ptr, return right half start
        first_half_end = self.firstHalfEnd(head)
        mid, first_half_end.next = first_half_end.next, None  # save and cut.
        return mid

    # find first half end node with slow & fast ptr
    def firstHalfEnd(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast.next and fast.next.next:  # 1234情况下返回2 12345返回3
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, l1, l2) -> ListNode:
        p = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                p.next, l1 = l1, l1.next
            else:
                p.next, l2 = l2, l2.next
            p = p.next
        p.next = l1 if l1 else l2
        return dummy.next

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head  # termination.
        mid = self.cut(head)
        left, right = self.sortList(head), self.sortList(mid)
        return self.merge(left, right)
