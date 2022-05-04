import collections
from heapq import heapify, heappop, heappush
from typing import List


class Solution:  # https://leetcode.cn/problems/alien-dictionary/submissions/
    """https://www.lintcode.com/problem/892/?_from=collection&fromId=161
    There is a new alien language which uses the latin alphabet. However,
    the order among letters are unknown to you.
    You receive a list of non-empty words from the dictionary,
    where words are sorted lexicographically by the rules of this new language.
    Derive the order of letters in this language.

    You may assume all letters are in lowercase.
    The dictionary is invalid, if string a is prefix of string b and b is appear before a.
    If the order is invalid, return an empty string.
    There may be multiple valid order of letters, return the smallest in normal lexicographical order.
    The letters in one string are of the same rank by default and are sorted in Human dictionary order.
    Example
    Example 1:

    Input：["wrt","wrf","er","ett","rftt"]
    Output："wertf"
    Explanation：
    from "wrt"and"wrf" ,we can get 't'<'f'
    from "wrt"and"er" ,we can get 'w'<'e'
    from "er"and"ett" ,we can get 'r'<'t'
    from "ett"and"rftt" ,we can get 'e'<'r'
    So return "wertf"
    Example 2:

    Input：["z","x"]
    Output："zx"
    Explanation：
    from "z" and "x"，we can get 'z' < 'x'
    So return "zx"
    Tags
    Breadth First Search/BFS, Topological Sort
    Company
    Twitter, Pocket Gems, Airbnb, Facebook, Snapchat, Google
    求字典序最小的拓扑序
    sequence reconstruction那题 是基于subsequence构造满足所有subsequence的
    shortest common supersequence, 既则把sequence当成path in graph 构图找到一个拓扑序即可
    本题比较难理解的地方, 和sequence reconstruction不同的地方在于
    sequence本身即可代表依赖关系 / directed edges, 可以直接基于他们构造图,
    而这里的input words中的word们 需要经过一层映射才能获得 真实的依赖关系 / directed edges
    实际字符的alien dictionary order才是真正的依赖关系 / 才能代表真正的directed edges
    因此构图时需要根据此字典序来构造边
    如何构造adjacency list graph 取决于如何提取字典序信息:
    先初始化每个节点:set()
    滑动窗口为2 遍历前n-1个word 编号i [0...n-2]
        同时遍历当前word 和 next word中的字符 index range j = range(较短的word长度)  "较短的" 是因为字典序里如果a是b的前缀 a出现在b的前面  我们只关心公共前缀
            同向双指针也局限于较短的那个词
            如果两单词在位置j不同 则说明这对字符满足这样 curr_word[j] < next_word[j] 的字典序 !!!这构成一条边!!! BREAK 滑动窗口到下一对词 因为这已经足够告诉我们 两词在字典序下先后关系
            如果j已经到头(j==较短的word长度-1) 当前词长度>next_word长度 则不合法 不满足题目规定的 a是b的前缀 a必须出现在b前面 按题目要求返回none
            因为words已经按字典序完全排序 所以这里不会出现别的情况 既一对同位置字符只能是 <=关系

    Python 解法，同樣為Topological sort模板
    Construct Graph時利用words順序前後的關係， 若為"abcgf", "abde"，可以找到c -> d，所以in_degree'd' += 1且neighbors'c'.append('d')
    Topological Sort時，由於題目規定要smallest in lexicographical order， 所以需要minimum heap來作為BFS的queue，python可用heapq方法來實作
        @param words: a list of words   sorted by the alien dictionary order 一个word列表 已经按字典序排序
        @return: a string which is correct order of all letters a-z (in this alien dictionary order)
    """

    def alienOrder(self, words: List[str]) -> str:
        graph = self.build_graph(words)
        if not graph:
            return ""
        return self.topo_sort(graph)  # 使用heap的常规topo sort

    def build_graph(self, words):  # 本体的难点在于构图
        graph = {}
        for seq in words:
            for char in seq:
                if char not in graph:
                    graph[char] = set()  # add all nodes to graph
        # for seq in words:
        #     for i in range(1, len(seq)):
        #         graph[seq[i - 1]].add(seq[i])
        n = len(words)
        for i in range(n - 1):  # 同时遍历2个单词的起点 所以i最大 n-2
            for j in range(
                min(len(words[i]), len(words[i + 1]))
            ):  # 指针j 同时遍历当前 next word
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(
                        words[i + 1][j]
                    )  # 不等的字符直接 代表 一条边
                    break
                if j == min(len(words[i]), len(words[i + 1])) - 1:  # j到头了
                    if len(words[i]) > len(
                        words[i + 1]
                    ):  # 不合法 a是b的前缀 不可以b出现在a之前 按题目要求返回none
                        return None
        return graph

    def get_indegree(self, graph):
        indegrees = {n: 0 for n in graph.keys()}
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                indegrees[neighbor] += 1
        return indegrees

    def topo_sort(self, graph):
        indegrees = self.get_indegree(graph)
        order = ""
        q = [n for n in graph.keys() if indegrees[n] == 0]
        heapify(q)
        while q:
            node = heappop(q)
            order += node
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    heappush(q, neighbor)
        if len(order) == len(graph):
            return order
        return ""
