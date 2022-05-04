class Solution:  # https://leetcode.cn/problems/rotate-list/?envType=study-plan-v2&envId=top-interview-150
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head
        n = 1
        # count linkedlist length
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        # new linkedlist tail 1-based index is n - k % n
        # if this tail is same as n, simply return head (this means we rotated k % n = 0 steps)
        if (add := n - k % n) == n:
            return head
        # cur is at old list tail, set next to head to make it a circle, move forward n-k%n step to reach the new tail
        # cut down the linkedlist at new tail and return <new tail>.next which is the new head
        cur.next = head
        while add:
            cur = cur.next
            add -= 1
        ret = cur.next
        cur.next = None
        return ret
