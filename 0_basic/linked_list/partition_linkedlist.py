class Solution:  # https://leetcode.cn/problems/partition-list/?envType=study-plan-v2&envId=top-interview-150
    # maintain a small linkedlist with all elements value < x and a large linkedlist .. > x
    # 3 pointers traverse original and update small and large linkedlists
    # finally attach small linkedlist end to large linkedlist start, set large traversal pointer curr2.next to None
    # O(n) O(1)
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1, dummy2 = ListNode(), ListNode()
        cur1, cur2, cur = dummy1, dummy2, head
        while cur:
            if cur.val < x:
                cur1.next = cur
                cur1 = cur1.next
            else:
                cur2.next = cur
                cur2 = cur2.next
            cur = cur.next
        cur1.next, cur2.next = dummy2.next, None
        return dummy1.next
