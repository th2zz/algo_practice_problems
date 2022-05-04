class Solution:
    """https://www.lintcode.com/problem/10/?_from=collection&fromId=161
    Description
Given a string, find all permutations of it without duplicates.

Example
Example 1:

Input:

s = "abb"
Output:

["abb", "bab", "bba"]
Explanation:

There are six kinds of full arrangement of abb, among which there are three kinds after removing duplicates.

Example 2:

Input:

s = "aabb"
Output:

["aabb", "abab", "baba", "bbaa", "abba", "baab"]
    @param str: A string
    @return: all permutations 给定一个有重复字符的 字符串 找到其所有无重复全排列
    搜索去重的诀窍 选有代表性的 在每组重复方案中选择代表方案 而不是将所有方案在hashset中去重 例如 100个a 100！方案不好全搞出来
    对于a1a2b 搜索过程中保持a2在a1的后面
        如 a1 a2 b1 b2 b3  a1a2b3 是不行的 b2没选就选了b3 和上面构成逆序
    搜索树
            " "
        /        \
       a1         b1  一开始只能选  a1或b1
     /   \      /    \
    a1a2 a1b1  b1a1 b1b2   不可以逆序选择 a1b2      b1a2 这是需要进行可行性剪枝的部分
    """
    def stringPermutation2(self, str):
        if not str:
            return [str]
        chars = list(sorted(str))  # 排序的目的时知道 当aaabbb发生时 知道现在是第几个重复的字符
        visited = [False] * len(chars)
        permutations = []
        self.dfs(chars, visited, [], permutations)
        return permutations

    def dfs(self, chars, visited, permutation, permutations):  # 递归的定义 求所有permutation为前缀的排列 visited: 当前permutation上有哪些字符被用过
        if len(permutation) == len(chars):  # 递归的出口 找到一个完整的排列
            permutations.append(''.join(permutation))
            return
        for i in range(len(chars)):  # 递归的拆解 基于当前排列前缀 下一个字符选啥
            if visited[i]:  # 需要通过visited bitmap来知道选过什么 保证构造排列过程中 不重复选择 TODO 避免a1a1的情况
                continue  # continue = 当前这个不行 试下一个字符
            if i > 0 and chars[i - 1] == chars[i] and not visited[i - 1]:  # dedup & pruning, 不能跳过一个a选下一个a 不同位置同样的字符 必须按顺序使用
                continue  # 如果前面字符和当前字符相同 前面没访问过 不应该跳过前面选当前的 否则会构成逆序 TODO 避免b1a2 a1b2的情况
            visited[i] = True
            permutation.append(chars[i])  # 找到所有permutation开头的排列
            self.dfs(chars, visited, permutation, permutations)  # 避免做字符串 + 操作 因为这是个O(n) space time的操作 n=len(str)
            permutation.pop()  # 前后做镜像操作来回溯  回到当前问题 下一个字符选啥: 下个字符尝试选别的
            visited[i] = False
