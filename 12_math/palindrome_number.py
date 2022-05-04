class Solution:
    # https://leetcode.cn/problems/palindrome-number/description/
    def isPalindrome(self, x: int) -> bool:
        # 末位为0或负数 
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        if x == 0:
            return True
        reverted_num = 0
        # 类似位运算题目 只不过这里是10进制
        # 取lsb from x (10进制) 构建结果 right shift truncate x lsb
        # 当反转数取到超过一半时 even: x == reverted num, odd x == reverted_num去掉最后一位
        while x > reverted_num:
            reverted_num = reverted_num * 10 + x % 10
            x = x // 10
        return x == reverted_num or x == (reverted_num // 10)