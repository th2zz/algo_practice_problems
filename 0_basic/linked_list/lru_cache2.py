class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key, self.value, self.next = key, value, next


class LRUCache:
    """
    https://www.lintcode.com/problem/134/?_from=collection&fromId=161
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations:
    get and set.

get(key) Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
Finally, you need to return the data from each get.

Example1

Input:
LRUCache(2)
set(2, 1)
set(1, 1)
get(2)
set(4, 1)
get(1)
get(2)
Output: [1,-1,1]
Explanation：
cache cap is 2，set(2,1)，set(1, 1)，get(2) and return 1，set(4,1) and delete (1,1)，
because （1,1）is the least use，get(1) and return -1，get(2) and return 1.
Example 2:

Input：
LRUCache(1)
set(2, 1)
get(2)
set(3, 2)
get(2)
get(3)
Output：[1,-1,2]
Explanation：
cache cap is 1，set(2,1)，get(2) and return 1，set(3,2) and delete (2,1)，get(2) and return -1，get(3) and return 2.
Hash Table
Doubly Linked List
Linked List
Related Problems
538
Memcache
Medium
24
LFU Cache
Hard
实现固定容量的lru缓存 需要实现
get(key) get一个key对应的值
set(key, value) set一个key的值 缓存满时需要淘汰least recently used item
    """

    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.dummy = LinkedNode()  # dummy head  实际的head为dummy.next
        self.tail = self.dummy  # 维护 tail指针
        self.key2prev = {}  # 维护一个 key: prev指针  map

    def put(self, key: int, value: int):
        return self.set(key=key, value=value)

    def set(self, key: int, value: int):
        if key in self.key2prev:  # 已经存在的key: 覆盖一下值 最近使用的都放到末尾
            self.move_node_to_tail(key)
            self.tail.value = value
            return
        self.push_back(LinkedNode(key, value))  # 不存在的key 直接append 末尾
        if len(self.key2prev) > self.capacity:  # 如果缓存已满 pop front = evict least recently used item
            self.pop_front()

    def get(self, key: int):
        if key not in self.key2prev:  # key 不存在于cache 返回-1
            return -1
        self.move_node_to_tail(key)  # 刚被访问过 应该移到链表末尾
        return self.tail.value  # 返回tail的值

    def push_back(self, node):  # append to the end 更新map信息和tail指针
        self.key2prev[node.key] = self.tail  # 添加 node.key: tail 到map
        self.tail.next = node  # 更新tail相关信息 tail.next = node,  tail设成node
        self.tail = node

    def pop_front(self):  # 将真的头删除 dummy.next指向新的头 更新map相关信息
        head = self.dummy.next  # 需要删除的头
        new_head = head.next
        self.dummy.next = new_head  # 更新real head  为要删除头的下一个
        self.key2prev[new_head.key] = self.dummy  # 更新 新的头的key_to_prev映射关系
        del self.key2prev[head.key]  # 从map中删除
        head.next = None

    # 将key节点移动到尾部: 从从链表中删掉节点, 更新map相关信息 push_back node追加到末尾
    def move_node_to_tail(self, key):
        prev = self.key2prev[key]  # 通过维护的key:prev map 获取prev 和 node 引用
        node = prev.next
        if node == self.tail:  # 幂等检查 node已经是tail 返回
            return
        # 删掉key对应的node 后 pushback
        prev.next = node.next  # prev.next跳过node
        self.key2prev[node.next.key] = prev  # 更新node下一个 key对应的prev节点 即prev
        node.next = None  # 断掉keynode 和下个节点的 连接
        self.push_back(node)  # TODO 加到链表末尾
