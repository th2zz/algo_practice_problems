# https://leetcode.cn/problems/substring-with-concatenation-of-all-words/description/?envType=study-plan-v2&envId=top-interview-150
import collections


class Solution:
    """
            Given a string, and a list of words
            find all consecutive concatenated substrings in s as a permutation of provided words
            return a list of starting indices of such substring
            Example 1:

    Input: s = "barfoothefoobarman", words = ["foo","bar"]

    Output: [0,9]

    Explanation:

    The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
    The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

    Example 2:

    Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

    Output: []

    Explanation:

    There is no concatenated substring.

    Example 3:

    Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

    Output: [6,9,12]

    Explanation:

    The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
    The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
    The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].
    """

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        k = len(words[0])  # assuming each word is of length k
        n = len(s)
        w = len(words)
        ans = []

        def increment(word, number, counter):
            count[word] += number
            if count[word] == 0:
                del count[word]

        for start in range(k):
            curr = start
            if curr + w * k > n:
                continue
            count = collections.Counter()
            for word in words:
                count[word] += 1
            for _ in range(w):
                increment(s[curr : curr + k], -1, count)
                curr += k
            if len(count) == 0:
                ans.append(curr - (w * k))
            while curr + k <= n:
                increment(s[curr : curr + k], -1, count)
                increment(s[curr - (w * k) : curr - ((w - 1) * k)], 1, count)
                curr += k
                if len(count) == 0:
                    ans.append(curr - (w * k))
            return ans
