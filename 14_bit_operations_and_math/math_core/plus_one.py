class Solution:
    # https://leetcode.cn/problems/plus-one/
    # found digit is not 9, add 1, clear remaining bits and return
    # all digits are 9, add additional 1, clear all bits as 0
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                for j in range(i + 1, len(digits)):
                    digits[j] = 0
                return digits
        return [1] + [0] * len(digits)