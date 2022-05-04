import collections


class Solution:
    """ https://www.lintcode.com/problem/616/?_from=collection&fromId=161
    返回任意拓扑序
    There may be multiple correct orders, you just need to return one of them.
    If it is impossible to finish all courses, return an empty array.
    Example
    Example 1:

    Input: n = 2, prerequisites = [[1,0]]  0是1的先修课 0->1
    Output: [0,1]
    Example 2:

    Input: n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,1,2,3] or [0,2,1,3]

        @param: numCourses: a total of n courses
        @param: prerequisites: a list of prerequisite pairs
        @return: the course order
        """

    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]  # adjacency list
        in_degree = [0] * numCourses
        for to_node, from_node in prerequisites:
            graph[from_node].append(to_node)
            in_degree[to_node] += 1
        q = collections.deque([i for i in range(numCourses) if in_degree[i] == 0])
        num_chosen = 0
        order = []
        while q:
            course_no = q.popleft()
            num_chosen += 1
            order.append(course_no)
            for next_course in graph[course_no]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    q.append(next_course)
        if num_chosen == numCourses:
            return order
        return []
