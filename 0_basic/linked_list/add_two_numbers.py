# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # number are represented in reverse order in linkedlist: 2->4->3 + 5->6->4 = 7->0->8
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 哨兵节点
        carry = 0  # 进位
        while l1 or l2 or carry:  # 有一个不是空节点，或者还有进位，就继续迭代
            # 节点值和进位加在一起
            s = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carry, lsb = divmod(s, 10)
            cur.next = ListNode(lsb)  # 每个节点保存一个数位
            cur = cur.next  # 下一个节点
            if l1:
                l1 = l1.next  # 下一个节点
            if l2:
                l2 = l2.next  # 下一个节点
        return dummy.next  # 哨兵节点的下一个节点就是头节点

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """相加两个链表形式表示的数  https://leetcode.cn/problems/add-two-numbers/
                O(n+m) O(n+m) 先2pass还原出数 计算结果 再还原成链表
                Description
        You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

        Example
        Example 1:

        Input: 7->1->6->null, 5->9->2->null
        Output: 2->1->9->null
        Explanation: 617 + 295 = 912, 912 to list:  2->1->9->null
        Example 2:

        Input:  3->1->5->null, 5->9->2->null
        Output: 8->0->8->null
        Explanation: 513 + 295 = 808, 808 to list: 8->0->8->null
        Tags
        Linked List
        Simulation
        Related Problems
        756
        Multiply Two Numbers
        Easy
        221
        Add Two Numbers II
        Medium
        655
        Add Strings
        Easy
        656
        Multiply Strings
        Medium

                simulate a half adder = O(max(n, m)) O(max(n, m)), but not good for production code
                n = length of l1, m = length l2
                O(n+m) O(n+m)
                Args:
                    l1 ():
                    l2 ():

                Returns:
                    结果 链表形式 1<-2<-3(HEAD)
        """
        num1 = ""
        num2 = ""
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        res = str(int(num1) + int(num2))
        head = ListNode(-1)
        p = head
        for i in reversed(res):
            p.next = ListNode(int(i))
            p = p.next
        return head.next
