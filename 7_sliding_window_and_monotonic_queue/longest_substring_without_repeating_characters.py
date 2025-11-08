class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150
        Given a string, find the length of the longest substring without repeating characters.
        Example
        Example 1:

        Input: "abcabcbb"
        Output: 3
        Explanation: The longest substring is "abc".
        Example 2:

        Input: "bbbbb"
        Output: 1
        Explanation: The longest substring is "b".
        Challenge
        time complexity O(n)
        Tags
        Same Direction Two Pointers
        Two Pointers
        Related Problems
        928 Longest Substring with At Most Two Distinct Characters Medium
        386 Longest Substring with At Most K Distinct Characters Medium

        brute force do it by looping O(n^2) O(1)

        invariant: l枚举起始位置 r指针第一轮后始终位于之前匹配的最长无重复子串的最后一个字符 r单调递增不重置
        最长无重复子串
        外层循环l指针遍历子串起始位置, 内层循环r指针遍历终止位置 若发现r的位置重复则打擂台更新 最大子串长度 并尝试新的起点l (因为对于这个起点已经无路可走了 只能换起点了)
        每轮移动l指针(起始位置) 需要同时将 前一个起点s[l-1]从visited删除
        第一轮之后的遍历: 每进行下一个起始位置 需要将前一个起始位置 值 从visited中删除 (还原visited状态) 然后尝试 继续move r找到下一个不重复的终止位置
        (继承了之前找到的 重合的部分的visited, 避免重复操作)
        遍历起始位置l 遍历终止位置r
        每当遇到一个重复的r 移动l并尝试继承之前的状态继续移动r, r没有必要重置到l的位置从新开始数长度 那样会需要n^2
        abccd
        l  r s[r] in visited {a, b, c}  update max_len = 3
        abccd
            l r   move l, pop a from visited, visited = {b, c},  r still in visited, do nothing
        abccd
            lr   move l, pop b from visited, visited = {c},  r still in visited, do nothing
        abccd
            l
            r   move l, pop c from visited, visited={}, r not in visited, add c to visited and move r, add d to visited and move r
                visited = {c, d}, r out of bound
                nothing to do, move l till l out of bound

        s = dvdf
        l=0
            l > 0: no
            r = 0  s[0] not in visited visited = {d}
            r = 1 s[1] not in visited visited = {d,v}
            r = 2 s[2] in visited loop break
            res = 2
        l=1
            l > 0 visited.remove(d) visited ={v}
            r=2 s[2] not in visited visited = {v,d}
            r=3 s[3] not in visited visited = {v,d,f}
            r=4
            res = 4-1=3
        l=2
           l > 0 visited.remove(d) visited = {v, f}
           r = 4
           res no change
        l=3
           l > 0 visited.remove(f) visited = {v}
           ...
        """
        if not s:
            return 0
        n = len(s)
        visited = set()
        res, r = 0, 0
        # traverse start pos, remove out of window char from visited, check the sliding window length,
        for l in range(n):
            if l > 0:
                visited.remove(s[l - 1])
            while r in range(n) and s[r] not in visited:
                visited.add(s[r])
                r += 1
            res = max(res, r - l)
            # traverse end pos and find max substr without repeated chars len
            # when find duplicate at r, reset and move on to next start pos, pop s[l-1] from visited
        return res
