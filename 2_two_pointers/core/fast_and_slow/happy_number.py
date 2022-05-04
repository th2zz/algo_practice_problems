class Solution:  # https://leetcode.cn/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit**2
            return total_sum

        slow = get_next(n)
        fast = get_next(get_next(n))
        # 先走一步 否则无法循环 循环准入为slow != fast
        while slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return slow == 1
