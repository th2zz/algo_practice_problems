class Solution:
    # https://leetcode.cn/problems/add-binary/description/
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        carry = 0
        res = ""
        for i in range(max(len(a), len(b))):
            digit_a = ord(a[i]) - ord("0") if i < len(a) else 0
            digit_b = ord(b[i]) - ord("0") if i < len(b) else 0
            # 0, 0 => 0
            total = digit_a + digit_b + carry
            # 1, 1 => 1, 0, 1 => 0
            carry = (total) // 2
            res = str(total % 2) + res
        if carry:
            res = str(carry) + res
        return res
