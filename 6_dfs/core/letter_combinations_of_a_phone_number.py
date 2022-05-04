KEYBOARD = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


class Solution:
    """https://www.lintcode.com/problem/425/?_from=collection&fromId=161

Given a digit string excluded 0 and 1, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.

1
2 ABC
3 DEF
4 GHI
5 JKL
6 MNO
7 PQRS
8 TUV
9 WXYZ
Although the answer above is in lexicographical order, your answer could be in any order you want.

Example 1:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
Explanation:
'2' could be 'a', 'b' or 'c'
'3' could be 'd', 'e' or 'f'

Example 2:
Input: "5"
Output: ["j", "k", "l"]

    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letter_combinations(self, digits: str):
        if not digits:
            return []
        combinations = []
        self.dfs(digits=digits, curr_idx=0, comb=[], combinations=combinations)
        return combinations

    # 递归的定义 在digits: str中 curr_idx开始 找到所有以comb为前缀的 字符组合
    # 递归的出口  curr_idx == len(digits) 找到了一个组合 加到结果集
    # 递归的拆解 和递进  对于当前的数字 int(digits[curr_idx]) 在键盘上对应的字符集上 尝试增加每个字符作为前缀下个字符 并找到所有组合
    def dfs(self, digits, curr_idx, comb, combinations):
        if curr_idx == len(digits):
            combinations.append(''.join(comb))
            return
        digit: int = int(digits[curr_idx])
        letters = KEYBOARD[digit]
        for c in letters:
            comb.append(c)
            self.dfs(digits, curr_idx + 1, comb, combinations)
            comb.pop()

    #
    # def letterCombinations(self, digits):
    #     combinations = []
    #     if not digits:
    #         return combinations
    #     self.dfs(digits, 0, "", combinations)
    #     return combinations
    #
    # def dfs(self, digits, index, combination, combinations):
    #     """dfs on given digital string "digits" e.g. 23456 to search for all possible letter combination
    #
    #     Args:
    #         digits (str): digital string  e.g. 23456
    #         index (int): current position in digital string
    #         combination (str): current combination, can be backtracked during recursion
    #         combinations (list): current solution set
    #
    #     Returns:
    #
    #     """
    #     if index == len(digits):
    #         combinations.append(combination)
    #         return
    #     digit = int(digits[index])
    #     letters = KEYBOARD[digit]
    #     for c in letters:  # traverse all possible char for current number
    #         self.dfs(digits, index + 1, combination + c, combinations)
    #         # no backtrack because of call by value, str is immutable, we are creating a lot of new str on the way
