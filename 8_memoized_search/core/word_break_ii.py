class Solution:
    """https://www.lintcode.com/problem/582/?_from=collection&fromId=161
    582 · Word Break II
Hard 36%

Given a string s and a dictionary of words dict, add spaces in s to construct a sentence
where each word is a valid dictionary word.

Return all such possible sentences.

Example 1:

Input："lintcode"，["de","ding","co","code","lint"]
Output：["lint code", "lint co de"]
Explanation：
insert a space is "lint code"，insert two spaces is "lint co de".
Example 2:

Input："a"，[]
Output：[]
Explanation：dict is null.
Tags
Partition DP
Memoization Search
Depth First Search/DFS
Dynamic Programming/DP
Company
Twitter
Snapchat
Dropbox
Uber
Google
Related Problems
680
Split String
Medium
107
Word Break
Medium
给定一个单词字典 和一个去掉空格的句子 返回 通过插入空格 可以构成的句子方案， 使得句子中的所有单词都存在于字典中
wordbreak 返回所有具体的方案
follow up
wordbreak返回方案个数  Ignore case
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences. / all ways s can be splited s.t. every word is in word dict once
    """

    # word break i 返回可行性 可以dp解决 也可以找到方案后判断方案数>0
    def wordBreak0(self, s, wordDict):
        n = len(s)
        dp = [False] * (n + 1)  # 前i位字符能否被wordDict中单词表示
        dp[0] = True
        for i in range(n):  # traverse start pos
            for j in range(i + 1, n + 1):  # traverse end pos, j用来直接访问dp, 最大值=n
                if dp[i] and (s[i:j] in wordDict):  # if dp[i] is ok and s[i:j] in wordDict
                    dp[j] = True
        return dp[n]

    def wordBreak(self, s, wordDict):  # word break ii返回所有具体方案
        if not wordDict:
            return []
        max_word_len = len(max(wordDict, key=len))
        return self.dfs(s, max_word_len, wordDict, {})  # TODO return !

    def dfs(self, s, max_word_len, wordDict, memo) -> list[
        str]:  # 递归的定义: 找到s串word break方案 break出的单词都需要出现在wordDict中, 最长单词长度max_word_len
        if not s:  # 递归的出口 当前s为空 没得拆分  定义 空字符串本身 word break方案数为1: 通过插入空格 可以构成的句子数量=1
            return []
        if s in memo:
            return memo[s]  # word break拆分结果 list
        partitions = []  # 结果集
        for prefix_len in range(1, len(s)):  # 枚举句子s 中前缀长度 [1, len(s) - 1] 不含完整s
            if prefix_len > max_word_len:  # 剪枝不可行的
                break
            prefix = s[:prefix_len]  # 根据枚举的长度获得前缀
            if prefix not in wordDict:  # 跳过字典中不存在的前缀 不可能作为第一个break点
                continue  # 递归的拆分和递进:
            rest_partitions: list[str] = self.dfs(s[prefix_len:], max_word_len, wordDict,
                                                  memo)  # 递归求解字符串剩余部分partition结果
            for partition in rest_partitions:  # 当前前缀词和子问题各种方案组合出一个完整方案 如"lint" + "co de" 加到结果集
                partitions.append(prefix + " " + partition)
        if s in wordDict:  # s本身如果在input wordDict中 也算一个方案 前面没有考虑长度为 len(s)的前缀
            partitions.append(s)
        memo[s] = partitions  # book keeping 当前s划分结果
        return partitions

    """word break iii 返回方案个数 ignore case
    """

    def initialize(self, wordDict: list[str]):
        max_len, lower_dict = 0, set()  # 把所有词转成小写 记录最长word长度
        for word in wordDict:
            max_len = max(max_len, len(word))
            lower_dict.add(word.lower())
        return max_len, lower_dict

    def wordBreak3(self, s: str, wordDict: list[str]):
        if not wordDict:
            return 0
        max_len, lower_dict = self.initialize(wordDict)
        # word break by dfs
        return self.memo_search(s.lower(), max_len, lower_dict, {})

    # 递归的定义: 在s中找到word break方案个数 单词最长为max_len 字典为lower_dict
    def memo_search(self, s, max_word_len, lower_dict, memo):
        if not s:  # 定义 空字符串本身 word break方案数为1: 通过插入空格 可以构成的句子数量=1
            return 1
        if s in memo:
            return memo[s]
        result = 0  # 当前s方案总数
        for prefix_len in range(1, len(s)):  # enumerate 前缀长度 不含完整s
            if prefix_len > max_word_len:  # pruning based on max len in all words
                break
            prefix = s[:prefix_len]
            if prefix not in lower_dict:  # skip if it is not in dict
                continue
            result += self.memo_search(s[prefix_len:], max_word_len, lower_dict, memo)
        if s in lower_dict:  # s本身在字典中 也是一个方案
            result += 1
        memo[s] = result
        return memo[s]

    # def wordBreak3(self, s, dict):
    #     if not s or not dict:
    #         return 0
    #     max_len, lower_dict = self.initialize(dict)
    #     # word break by dfs
    #     return self.memo_search(s.lower(), 0, max_len, lower_dict, {})
    #
    # # 递归的定义: 在s中从index开始找到word break方案个数 单词最长为max_len 字典为lower_dict
    # def memo_search(self, s, index, max_len, lower_dict, memo):
    #     if index == len(s):
    #         return 1
    #     if index in memo:  # s[index..] processed before, return result
    #         return memo[index]
    #     result = 0  # s[index..] 方案总数
    #     for end in range(index + 1, len(s) + 1):  # enumerate word end;  end range [index + 1, len(s)]
    #         if end - index > max_len:  # pruning based on max len in all words
    #             break  # end - index = [index, ..., end - 1] [index...]substring length
    #         word = s[index: end]  # get s substring [index, ..., end - 1] as word
    #         if word not in lower_dict:  # skip if it is not in dict
    #             continue  # recurse on s[end..] add that to current result
    #         result += self.memo_search(s, end, max_len, lower_dict, memo)  # 这个word end就是下个word开始index
    #     memo[index] = result  # memo: # possible sentences formed from s[index..]
    #     return memo[index]  # original problem solution: memo[0]
