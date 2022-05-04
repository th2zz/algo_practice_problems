"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """https://www.lintcode.com/problem/228/?_from=collection&fromId=161
    Description
Find the middle node of a linked list and return it.

Example
Example 1:

Input:  1->2->3
Output: 2
Explanation: return the middle node.
Example 2:

Input:  1->2
Output: 1
Explanation: If the length of list is even return the center left one.
Challenge
If the linked list is a data stream, can you find the middle node without iterating the linked list again?

Tags
Same Direction Two Pointers
Linked List
Two Pointers
Related Problems
174
Remove Nth Node From End of List
Easy

Naive: first find length l with one pass, find middle in second pass
follow up: can you do it in one pass ? this is a very concrete and useful engineering use case: data stream problems

    @param head: the head of linked list.
    @return: a middle node of the linked list
    """

    def middleNode(self, head):
        # write your code here
        if not head:
            return head
        slow, fast = head, head.next  # TODO 偶数节点情况下 返回左半边 需要fast从head.next开始
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def middleNode2(self, head):
        slow, fast = head, head  # TODO 偶数节点情况下返回右半边 或无所谓 可以同时从head开始
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
