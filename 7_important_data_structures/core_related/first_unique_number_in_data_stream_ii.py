class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key, self.value, self.next = key, value, next


class DataStream:
    # https://www.lintcode.com/problem/960/?_from=collection&fromId=161
    # medium
    """
We need to implement a data structure named DataStream. There are two methods required to be implemented:
void add(number) // add a new number
int firstUnique() // return first unique number
You can assume that there must be at least one unique number in the stream when calling the firstUnique.

Example 1:

Input:
add(1)
add(2)
firstUnique()
add(1)
firstUnique()
Output:
[1,2]
Example 2:

Input:
add(1)
add(2)
add(3)
add(4)
add(5)
firstUnique()
add(1)
firstUnique()
add(2)
firstUnique()
add(3)
firstUnique()
add(4)
firstUnique()
add(5)
add(6)
firstUnique()
Output:
[1,2,3,4,5,6]
Tags
Hash Table
Data Stream
Related Problems
685
First Unique Number in Data Stream
Medium
646
First Position Unique Character
Easy
209
First Unique Character in a String
Easy
    """

    def __init__(self):
        self.dummy = LinkedNode()  # 维系一个unique node链表 出现仅1次的
        self.tail = self.dummy
        self.key2prev = {}  # 出现仅1次的
        self.duplicates = set()  # 出现至少2次的数

    def push_back(self, node):
        self.key2prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    def remove(self, num):
        prev = self.key2prev[num]
        node = prev.next  # 获取prev 和 node引用
        next = node.next
        prev.next = next  # prev跳过node指向其下一个
        node.next = None  # 删掉node.next链
        del self.key2prev[num]  # 删除map中信息
        if next:  # 刚删的不是tail 正常增加map信息
            self.key2prev[next.key] = prev
        else:  # 刚删的"node"是tail 更新tail
            self.tail = prev

    """
    @param num: next number in stream
    @return: nothing
    """

    def add(self, num):  # O(1)
        if num in self.duplicates:  # 第二次及以上遇到 已经在duplicates, 重复直接返回
            return
        if num not in self.key2prev:  # 第一次遇到: self.key2prev维护了独特num链表信息, 加入链表并更新信息
            self.push_back(LinkedNode(num))
        else:  # 第二次遇到 加到duplicate 从链表和map删除
            self.duplicates.add(num)
            self.remove(num)

    """
    @return: the first unique number in stream
    """

    def firstUnique(self):  # O(1)
        return self.dummy.next.key

    # def __init__(self):
    #     self.nums = []
    #     self.num2cnt = {}
    #
    # """
    # @param num: next number in stream
    # @return: nothing
    # """
    # def add(self, num): # O(1)
    #     self.nums.append(num)
    #     self.num2cnt[num] = self.num2cnt.get(num, 0) + 1
    #
    # """
    # @return: the first unique number in stream
    # """
    # def firstUnique(self):  # O(n)
    #     for n in self.nums:
    #         if self.num2cnt[n] == 1:
    #             return n
