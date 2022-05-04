import random


class RandomizedSet:
    """
    https://www.lintcode.com/problem/657/?_from=collection&fromId=161
    Description
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
Tags
Hash Table
Company
Twitter
Amazon
Facebook
Uber
Google
Related Problems
954
Insert Delete GetRandom O(1) - Duplicates allowed
Hard
设计一种数据结构 支持 插入删除getRandom O(1) on average, 假设无重复元素   getRandom return 1 element uniformly at random
(each element with same probabilty of getting returned)
    """

    def __init__(self):
        self.nums, self.valToindexDict = [], {}  # 维护一个数组 和 val:index map

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """

    def insert(self, val):  # 插入: O(1)过滤已经存在情况 直接append到数组 添加val:idx 关系到map
        if val in self.valToindexDict:
            return False
        self.nums.append(val)
        self.valToindexDict[val] = len(self.nums) - 1
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """

    def remove(self, val):  # 删除: O(1)过滤不存在情况 根据维护的val:idx关系 交换尾部元素 删除尾部元素 删除map中val entry
        if val not in self.valToindexDict:
            return False
        index_of_val = self.valToindexDict[val]
        last_val = self.nums[-1]
        self.nums[index_of_val] = last_val  # val不是最后一个元素 把最后一个元素放到val位置上
        self.valToindexDict[last_val] = index_of_val
        self.nums.pop()  # 无脑delete last element O(1)
        del self.valToindexDict[val]
        return True

    """
    @return: Get a random element from the set
    """

    def getRandom(self):  # getRandom 直接获取一个随机index
        return self.nums[random.randint(0, len(self.nums) - 1)]  # random.randint(a,b) return 1 int in interval [a,b]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
