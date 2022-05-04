class TwoSum:
    """https://www.lintcode.com/problem/607/
    Description 使用一个hashtable add时维护频次 find = O(n)遍历hashtable根据cnt判断另一半是否存在 判断时要考虑到两数大小关系
    Design and implement a TwoSum class. It should support the following operations: add and find.

    add - Add the number to an internal data structure.
    find - Find if there exists any pair of numbers which sum is equal to the value.

    Example
    Example 1:

    add(1); add(3); add(5);
    find(4) // return true
    find(7) // return false
    """

    def __init__(self):
        self.num_to_cnt_map = {}  # 维护一个 num: cnt map

    """
    @param number: An integer
    @return: nothing
    """

    def add(self, number):  # 计数表中+1
        self.num_to_cnt_map[number] = self.num_to_cnt_map.get(number, 0) + 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers that sum up to target value.
    """

    def find(self, value):  # 看表数数 够不够  相同的数至少2 不同至少1
        for num1 in self.num_to_cnt_map.keys():
            num2 = value - num1
            num2cnt = 2 if num1 == num2 else 1  # 需要达到的num2 count
            if self.num_to_cnt_map.get(num2, 0) >= num2cnt:  # counterpart存在 twosum有解需要达到的条件
                return True
        return False

    def twoSum(self, nums, target):  # 基于hashmap的朴素2sum
        table = {}
        for i, num in enumerate(nums):
            if target - num in table:
                return [table[target - num], i]
            table[num] = i
        return []

    """
        @param value: An integer
        @return: Find if there exists any pair of numbers which sum is equal to the value.
        """

    def find_2p(self, value, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum > value:
                right -= 1
            elif sum < value:
                left += 1
            elif sum == value:
                return True
        return False

# a = TwoSum()
# a.add(1)
# a.add(3)
# a.add(5)
# print(a.find(4))
# print(a.find(7))
