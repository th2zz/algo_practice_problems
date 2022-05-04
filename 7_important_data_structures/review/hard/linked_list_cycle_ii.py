"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """https://www.lintcode.com/problem/103/?fromId=161&_from=collection
Description
Given a linked list, return the node where the cycle begins.

If there is no cycle, return null.

Example
Example 1:

Input:

null, no cycle
Output:

no cycle
Explanation:

List is null, so no cycle.
Example 2:

Input:

-21->10->4->5，tail connects to node index 1
Output:

10
Explanation:

The last node 5 points to the node whose index is 1, which is 10, so the entrance of the ring is 10

Challenge
Can you solve it without using extra space?

Tags
Same Direction Two Pointers
Linked List
Two Pointers
Related Problems
1229
Circular Array Loop
Medium
633
Find the Duplicate Number
Hard
380
Intersection of Two Linked Lists
Medium
    @param head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        pass