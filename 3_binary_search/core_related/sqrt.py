class Solution:
    # https://leetcode.cn/problems/sqrtx/
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        l, r = 0, x
        while l + 1 < r:
            m = l + (r - l) // 2
            if m**2 > x:
                r = m
            elif m**2 < x:
                l = m
            else:
                return m
        if r**2 < x:
            return r
        if l**2 < x:
            return l
        return l