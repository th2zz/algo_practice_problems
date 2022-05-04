# https://leetcode.cn/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150
# 判断是不是回文串 非法字符需跳过
class Solution:
    """

    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

    Have you consider that the string might be empty? This is a good question to ask during an interview.

    For the purpose of this problem, we define empty string as valid palindrome.

    Example
    Example 1:

    Input: "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama"
    Example 2:

    Input: "race a car"
    Output: false
    Explanation: "raceacar"
    Challenge
    O(n) time without extra memory.

    Tags
    Two Pointers
    Company
    LinkedIn
    Facebook
    Zenefits
    Microsoft
    Uber
    Related Problems
    893
    Longest Palindromic Substring II
    Hard
    891
    Valid Palindrome II
    Medium
    745
    Palindromic Ranges
    Medium
    744
    Sum of first K even-length Palindrome numbers
    Medium
    491
    Palindrome Number
    Easy
    627
    Longest Palindrome
    Easy
    223
    Palindrome Linked List
    Medium
    200
    Longest Palindromic Substring
    Medium
        @param s: A string
        @return: Whether the string is a valid palindrome
    """

    def is_char_valid(self, char):
        return char.isdigit() or char.isalpha()

    def isPalindrome(self, s):  # 相向双指针
        if not s or (s and len(s) == 1):
            return True
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not self.is_char_valid(s[left]):  # 跳过特殊字符
                left += 1
            while left < right and not self.is_char_valid(s[right]):
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():  # 不等立刻返回
                    return False
                left += 1
                right -= 1
        return True


# follow up 可以删除最多一个字符, 没有不合法字符 判断是不是palindrome   巧用子函数避免重复代码
# https://www.lintcode.com/problem/valid-palindrome-ii/
class Solution2:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character

    #重点 如何 查看first different pair [开始...结束] 的子串去掉left or right end是不是palindrome;
    inductively, this is to check 2 subproblem solution
    self.is_palindrome(s[left + 1:right + 1])[0] 去掉左端
    self.is_palindrome(s[left:right])[0] 去掉右端
    """

    def valid_palindrome(self, s: str) -> bool:
        if not s or (s and len(s) == 1):
            return True
        s_is_palindrome, left, right = self.is_palindrome(s)
        del_1_char_is_palindrome = (
            self.is_palindrome(s[left + 1 : right + 1])[0]
            or self.is_palindrome(s[left:right])[0]
        )
        return True if s_is_palindrome else del_1_char_is_palindrome

    def is_palindrome(self, s):  # return is_palindrome, first different pair index
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False, left, right
            left += 1
            right -= 1
        return True, left, right

    # def find_first_different_pair(self, s, left, right):
    #     while left < right:  # this is where >= comes from
    #         if s[left] != s[right]:
    #             return left, right
    #         left += 1
    #         right -= 1
    #     return left, right

    # def validPalindrome(self, s):
    #     if not s:
    #         return False
    #     s_is_palindrome, l, r = self.is_palindrome(s, 0, len(s) - 1)  # l, r = the first different pair if s is not palindrome
    #     return True if s_is_palindrome else self.is_palindrome(s, l + 1, r)[0] or self.is_palindrome(s, l, r - 1)[0]
    #     # 查看first different pair [开始...结束] 的子串去掉left or right end是不是palindrome; 是则可以做到

    # def is_palindrome(self, s, left, right):
    #     l, r = self.find_first_different_pair(s, left, right)
    #     return l >= r, l, r  # >=: 交错或重叠状态 说明没有找到first different pair == s is palindrome
