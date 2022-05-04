from collections import defaultdict


# https://leetcode.cn/problems/valid-anagram/description/
class Solution:
    # anagram: same sequence but can be different char order
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table = defaultdict(int)
        for c in s:
            table[c] += 1
        for c in t:
            table[c] -= 1
        for v in table.values():
            if v != 0:
                return False
        return True
