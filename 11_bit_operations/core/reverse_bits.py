class Solution:
    # https://leetcode.cn/problems/reverse-bits/
    def reverseBits(self, n: int) -> int:
        # assuming input length 32
        res = 0
        for i in range(32):
            lsb = n & 1
            res = (res << 1) | lsb
            n >>= 1
        return res