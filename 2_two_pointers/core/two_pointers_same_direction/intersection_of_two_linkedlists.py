class Solution:
    # 假设链表1有a个节点 2有b个节点 从intersection到末尾有c个节点
    # 对于链表1 开始到intersection有a-c个节点 链表2 开始到intersection有b-c个节点
    # 双指针同时遍历两个链表 A走完链表1 a个节点后去遍历链表2 B走完链表2 b个节点后去遍历链表1 a
    # 此时A走b-c个节点 B走a-c个节点后 两者会相遇 因为 a+b-c=b+a-c 相遇点为交点
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
