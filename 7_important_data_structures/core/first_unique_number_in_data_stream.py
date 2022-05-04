class Solution:
    """https://www.lintcode.com/problem/685/?_from=collection&fromId=161
    Description
Given a continuous stream of data, write a function that returns the first unique number (including the last number)
when the terminating number arrives. If the terminating number is not found, return -1.

Example
Example1

Input:
[1, 2, 2, 1, 3, 4, 4, 5, 6]
5
Output: 3
Example2

Input:
[1, 2, 2, 1, 3, 4, 4, 5, 6]
7
Output: -1
Example3

Input:
[1, 2, 2, 1, 3, 4]
3
Output: 3
    @param nums: a continuous stream of numbers
    @param number: the terminating number
    @return: returns the first unique number up to and including the terminating number
找到连续的数据流中 遇到终止数前 第一个独特的数
如果终止数不存在于数据流中 返回-1
终止数本身也可以是独特的数
    """

    def firstUniqueNumber(self, nums, number):
        if not nums:
            return -1
        table = {}
        for num in nums:
            table[num] = table.get(num, 0) + 1
            if num == number:
                break
        else:  # 只有当循环里没有遇到 break 时，for else的 else 块才会执行
            return -1  # terminating number not found
        for num, cnt in table.items():
            if cnt == 1:
                return num
            # 这段代码可以没有 if terminate number not found already returned,
            # found and > 1 times is not possible because of first break
            # found and == 1 times already returned in the above if
            # if num == number:
            #     break
        return -1
