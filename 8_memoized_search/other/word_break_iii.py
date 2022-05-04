class Solution:
    """https://www.lintcode.com/problem/683/?_from=collection&fromId=161
Medium
Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by
inserting whitespaces to the sentence so that each word can be found in the dictionary.
给定一个单词字典 和一个去掉空格的句子 返回 通过插入空格 可以构成的句子数量， 使得句子中的单词都存在于字典中
Ignore case

Example
Example1

Input:
"CatMat"
["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
Output: 3
Explanation:
we can form 3 sentences, as follows:
"CatMat" = "Cat" + "Mat"
"CatMat" = "Ca" + "tM" + "at"
"CatMat" = "C" + "at" + "Mat"
Example1

Input:
"a"
[]
Output:
0

Tags
Dynamic Programming/DP
Partition DP

给定一个单词字典 和一个去掉空格的句子 返回 通过插入空格 可以构成的句子数量， 使得句子中的单词都存在于字典中
wordbreak返回方案个数  Ignore case
    @param s: A string
    @param dict: A set of word
    @return: the number of possible sentences. / how many ways to form the sentence with given words in dict & space
    can we use a word multiple times: no
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
