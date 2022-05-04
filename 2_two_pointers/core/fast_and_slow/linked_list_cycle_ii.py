class Solution(object):
    def detectCycle(self, head):
        """Return cycle start
        :type head: ListNode
        :rtype: ListNode
        """
        has_cycle = False
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                has_cycle = True
                break
        if has_cycle:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
