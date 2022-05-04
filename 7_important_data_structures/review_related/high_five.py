'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
"""
Algorithms
Medium
Accepted Rate
45%

DescriptionSolutionNotesDiscussLeaderboard
Description
Each student has two attributes ID and scores. Find the average of the top five scores for each student.

Example
Example 1:

Input: 
[[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]
Output:
1: 72.40
2: 97.40
Example 2:

Input:
[[1,90],[1,90],[1,90],[1,90],[1,90],[1,90]]
Output: 
1: 90.00
Tags
Hash Table
Heap
Company
Amazon
Related Problems
544
Top k Largest Numbers
Medium
"""
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        pass