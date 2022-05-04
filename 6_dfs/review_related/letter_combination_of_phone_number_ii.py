from typing import (
    List,
)

class Solution:
    """
    Algorithms
Medium
Accepted Rate
47%

DescriptionSolutionNotesDiscussLeaderboard
Description
Given some digit strings excluded 0 and 1 and a dict, for each digit string
return the number of possible letter combinations in dict that the number could match.

If we can use a digit string represent the prefix of a word, we think they can match.

A mapping of digit to letters (just like on the telephone buttons) is given below.

KEYBOARD = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

words only contain lowercase letters.
1 \leq len(queries) \leq 10^31≤len(queries)≤10^3
1 \leq \sum |queries_i| \leq 5 \times 10^4
1 \leq len(dict) \leq 10^31≤len(dict)≤10^3
1 \leq \sum |dict_i| \leq 5 * 10^4
Example
Example 1

Input: query = ["2", "3", "4"]
dict = ["a","abc","de","fg"]
Output:[2,2,0]
Explanation:
"a" "abc" match "2"
"de" "fg" match "3"
no word match "4"
Tags
Trie
    """
    """
    @param queries: the queries
    @param dict: the words
    @return: return the queries' answer
    """
    def letter_combinations_i_i(self, queries: List[str], dict: List[str]) -> List[int]:
        # write your code here
        pass