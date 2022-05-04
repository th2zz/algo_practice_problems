# https://leetcode.cn/problems/merge-k-sorted-lists/?favorite=2cktkvj

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # merge linkedlists like merge 2 arrays
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur = dummy
        p1, p2 = list1, list2
        while p1 and p2:  # O(min(n,m)) = O(n+m)
            if p1.val <= p2.val:
                cur.next = p1
                l1_remains = p1.next
                p1.next = None
                p1 = l1_remains
            else:
                cur.next = p2
                l2_remains = p2.next
                p2.next = None
                p2 = l2_remains
            cur = cur.next
        # O(|n-m|)
        if p1:
            cur.next = p1
        elif p2:
            cur.next = p2
        return dummy.next  # Time O(max(n,m)) Space O(1)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        return self.merge_helper(0, len(lists) - 1, lists)

    """ divde and conquer like merge sort
    assume N=total #nodes, k=#linkedlists, recursion tree height logk, each layer work is bounded by O(N)
    Time O(Nlogk) Space O(logk)
    an iterative optimized version can take O(1) space
    """

    def merge_helper(self, start, end, lists):
        if start >= end:
            return lists[start]
        mid = (start + end) // 2
        left_res = self.merge_helper(start, mid, lists)
        right_res = self.merge_helper(mid + 1, end, lists)
        return self.mergeTwoLists(left_res, right_res)
