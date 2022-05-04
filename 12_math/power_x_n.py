class Solution:
    # 快速幂算法 只在指数为1的位置 去快速乘上每轮 通过自乘 a*=a指数指数增长的a 
    # e.g. a = 2^2 2^4 2^8 2^16
    # 根据幂指数运算规则 2^10 = 2^2 * 2^8 = 2^(2 + 8)
    # 10二进制表示为1010  遍历指数每一个lsb 并不断rightshift
    # if lsb == 1:  res *= 该位置 a的值 也即快速幂子问题解
    # 同时循环时记录 a每轮快速幂子问题解, b bitshift
    # a=2 b=10

    # b = 1010 
    # res = 0
    # a = 2^2 b=101

    # b = 101
    # res = 1 * 2^2
    # a = 2^4 b = 10

    # b = 10
    # res = 2^2
    # a = 2^8 b = 1

    # b = 1
    # res = 2^2 *2^8 = 2^10
    # a = 2^16 b = 0 exit loop
    def pow(self, a: float, b: int) -> float:
        res = 1
        while b > 0:
            if b & 1:
                res *= a
            a *= a
            b >>= 1
        return res

    def myPow(self, x: float, n: int) -> float:
        return self.pow(x, n) if n > 0 else 1.0 / self.pow(x, -n)