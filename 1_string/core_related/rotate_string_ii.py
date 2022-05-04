class Solution:
    """https://www.lintcode.com/problem/1790/?_from=collection&fromId=161
根据total offset left rotate / right rotate str
Given a string(Given in the way of char array), a right offset and a left offset, move the string according to the
given offset and save it in a new result set.
(left offest represents the offset of a string to the left,
right offest represents the offset of a string to the right,
the total offset is calculated from the left offset and the right offset,
split two strings at the total offset and swap positions)。

Example
Example 1:

Input：str ="abcdefg", left = 3, right = 1
Output："cdefgab"
Explanation：The left offset is 3, the right offset is 1, and the total offset is left 2. Therefore, the original string
moves to the left and becomes "cdefg"+ "ab".
Example 2:

Input：str="abcdefg", left = 0, right = 0
Output："abcdefg"
Explanation：The left offset is 0, the right offset is 0, and the total offset is 0. So the string remains unchanged.
Example 3:

Input：str = "abcdefg",left = 1, right = 2
Output："gabcdef"
Explanation：The left offset is 1, the right offset is 2, and the total offset is right 1. Therefore,
the original string moves to the left and becomes "g" + "abcdef".
Tags
String
Company
LinkedIn
    @param str: An array of char
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """

    def RotateString2(self, str, left, right):
        total_offset = (left - right) % len(str)  # 需要注意mod! 否则大数left,right无法处理
        if total_offset > 0:  # rotate left by total_offset chars
            return str[total_offset:] + str[:total_offset]
        elif total_offset < 0:  # rotate right by -total_offset chars
            shift = - total_offset
            return str[total_offset:] + str[:len(str) - shift]
        return str