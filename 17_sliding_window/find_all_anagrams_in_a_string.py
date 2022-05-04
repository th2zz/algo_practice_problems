from collections import Counter
from typing import List


class Solution:
    # find all anagrams of pattern p in s, return list of start idx
    # Input: s = "cbaebabacd", p = "abc" Output: [0,6]
    # Input: s = "abab", p = "ab", Output: [0,1,2]
    # https://leetcode.cn/problems/find-all-anagrams-in-a-string/solutions/2969498/liang-chong-fang-fa-ding-chang-hua-chuan-14pd
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        cnt = Counter(p)  # 统计 p 的每种字母的出现次数
        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1  # 右端点字母进入窗口
            while cnt[c] < 0:  # 字母 c 太多了
                cnt[s[left]] += 1  # 左端点字母离开窗口
                left += 1
            if right - left + 1 == len(p):  # s' 和 p 的每种字母的出现次数都相同
                ans.append(left)  # s' 左端点下标加入答案
        return ans

    def findAnagrams2(self, s: str, p: str) -> List[int]:
        ans = []
        cnt_p = Counter(p)  # 统计 p 的每种字母的出现次数
        cnt_s = Counter()  # 统计 s 的长为 len(p) 的子串 s' 的每种字母的出现次数
        for right, c in enumerate(s):
            cnt_s[c] += 1  # 右端点字母进入窗口
            left = right - len(p) + 1
            if left < 0:  # 窗口长度不足 len(p)
                continue
            if cnt_s == cnt_p:  # s' 和 p 的每种字母的出现次数都相同
                ans.append(left)  # s' 左端点下标加入答案
            cnt_s[s[left]] -= 1  # 左端点字母离开窗口
        return ans


sol = Solution()
assert sol.findAnagrams(s="abab", p="ab") == [0, 1, 2]
assert sol.findAnagrams(s="cbaebabacd", p="abc") == [0, 6]


# cnt = {"a": 1, "b": 1}, left=0
# right = 0, c = a
#    cnt =  {"a": 0, "b": 1} 1!=2 no update to ans
# right = 1, c = b
#    cnt = {"a": 0, "b": 0} 2==2  add left 0 to ans
# right = 2, c = a
#    cnt = {"a": -1, "b": 0}
#    too much a, enter loop to move left window boundary
#        {"a": 0, "b": 0} left = 1
#    2==2 add left 1 to answer
# right = 3, c = b
#    {"a": 0, "b": -1}
#    too much b, enter loop to move left window boundary
#        {"a": 0, "b": 0} left = 2
#    2==2 add left 2 to answer
