class TopK:
    """https://www.lintcode.com/problem/550/
    Description
Find top k frequent words in realtime data stream.

Implement three methods for Topk Class:

TopK(k). The constructor.
add(word). Add a new word.
topk(). Get the current top k frequent words.
If two words have the same frequency, rank them by dictionary order.

Example
Example 1:

Input：
TopK(2)
add("lint")
add("code")
add("code")
topk()
Output：["code", "lint"]
Explanation：
"code" appears twice and "lint" appears once, they are the two most frequent words.
Example 2:

Input：
TopK(1)
add("aa")
add("ab")
topk()
Output：["aa"]
Explanation：
"aa" and "ab" appear once , but aa's dictionary order is less than ab's.
Tags
Balanced Binary Tree
Heap
Data Stream
Related Problems
1883
Top K Frequently Mentioned Keywords
Medium
549
Top K Frequent Words (Map Reduce)
Medium
545
Top k Largest Numbers II
Medium
544
Top k Largest Numbers
Medium
471
Top K Frequent Words
Medium
    """
    """
    @param: k: An integer
    """

    def __init__(self, k):
        pass

    """
    @param: word: A string
    @return: nothing
    """

    def add(self, word):
        pass

    """
    @return: the current top k frequent words.
    """

    def topk(self):
        pass
