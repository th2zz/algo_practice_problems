"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    """
    https://www.lintcode.com/problem/105 medium
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.

Challenge
Could you solve it with O(1) space?
Related Problems
375
Clone Binary Tree
    """

    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        """
        please see the problme 137 clone graph.
        use the hash map/ dict to mapping the node: new node
        Space: O(n)
        """
        if not head:
            return head
        old2new = {}
        curr = head
        while curr:  # old2new the node to new node
            old2new[curr] = RandomListNode(curr.label)
            curr = curr.next
        for node, new_node in old2new.items():  # copy the next and ramdon pointer
            if node.next:
                new_node.next = old2new[node.next]
            if node.random:
                new_node.random = old2new[node.random]
        return old2new[head]
