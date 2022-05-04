import collections
from typing import Set


class Solution:
    """https://www.lintcode.com/problem/120/?_from=collection&fromId=161
    Description
Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end,
output the length of the sequence.
Transformation rule such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary. (Start and end words do not need to appear in the dictionary )
Return 0 if there is no such transformation sequence.

All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the dictionary.
You may assume beginWord and endWord are non-empty and are not the same.
len(dict) <= 5000, len(start) < 5len(dict)<=5000,len(start)<5

Example 1:
Input:
start = "a"
end = "c"
dict =["a","b","c"]
Output:
2
Explanation:
"a"->"c"

Example 2:
Input:
start ="hit"
end = "cog"
dict =["hot","dot","dog","lot","log"]
Output:
5
Explanation:
"hit"->"hot"->"dot"->"dog"->"cog"

简单图最短路径 uniform cost search with bfs
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: length of the shortest transformation sequence for transforming start to end by using intermediate words in dict
    """

    def ladder_length(self, start: str, end: str, dict: Set[str]) -> int:
        dict.add(end)
        # TODO 这里初始化为1因为题目要求 length of transformation sequence 端点个数而不是edge长度
        q = collections.deque([start])
        # distance to each node(transformed str) from start with rules "changing 1 char at a time"
        distance = {start: 1}
        while q:
            word = q.popleft()
            if word == end:
                return distance[word]
            for next_word in self.get_next_words(word, dict):
                if next_word not in distance:
                    q.append(next_word)
                    distance[next_word] = distance[word] + 1
        return 0

    # find all words that can be laddered after the word by modifying 1 char only
    # e.g. word = 'hot' d = {'hot', 'hit', 'hog'}, return {'hit', 'hog'}
    def get_next_words(self, word, d):
        next_words = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == c:  # skip same char
                    continue
                # switch character at index i to new char to generate new word
                new_word = word[:i] + c + word[i + 1:]
                if new_word in d:
                    next_words.append(new_word)
        return next_words

    def ladderLength1(self, start, end, d):  # by level order traversal
        # assume dict not none; assume beginWord and endWord non empty and not equal
        d.add(end)  # must add end, start in dict or not does not matter
        queue = collections.deque([start])
        visited = {start}
        distance = 0
        while queue:
            distance += 1  # length to current level 实际上也是修改次数
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == end:  # if reach target word return result
                    return distance
                for next_word in self.get_next_words(word, d):
                    if next_word not in visited:
                        queue.append(next_word)
                        visited.add(next_word)
        return 0
