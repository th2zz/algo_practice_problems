class Solution:  # https://leetcode-cn.com/problems/counting-bits/
    def hammingWeight(self, n: int) -> int:  # return #1s in binary representation of n
        res = 0
        while n:
            res += (n & 1)  # n&1 数一个1后 n right shift 1位
            n >>= 1
        return res

    def hamming_weight(self, n):
        res = 0
        while n:
            res += 1
            n &= n - 1  # &n-1可以清零尾部1, 每计数一次 清零一个尾部1
        return res

    # given int n, 返回n+1长度数组: 位置i为i的hamming weight(二进制表示中1的个数)  O(nlogn)
    def countBits(self, n: int) -> List[int]:
        return [self.hamming_weight(i) for i in range(n + 1)]

    # O(n) O(1)  dynamic programming
    def countBits1(self, n: int) -> List[int]:
        ones = [0]  # ones[i] = i的二进制中1的个数
        # 当前i二进制中1的个数 = ones[i >> 1]最后一位之前的1的个数 + i & 1 最后位是否为1
        for i in range(1, n + 1):
            ones.append(ones[i // 2] + (i & 1))
        return ones
