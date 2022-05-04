class Solution:
    """https://leetcode.cn/problems/course-schedule/description/
    There are a total of n courses you have to take, labeled from 0 to n - 1.
    Before taking some courses, you need to take other courses. For example, to learn course 0,
    you need to learn course 1 first, which is expressed as [0,1].
    Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
    现在你总共有 n 门课需要选，记为 0 到 n - 1.
    一些课程在修之前需要先修另外的一些课程，比如要学习课程 0 你需要先学习课程 1 ，表示为[0,1]
    ，判断是否可能完成所有课程
    样例
    例1:
    输入: n = 2, prerequisites = [[1,0]]
    输出: true
    例2:
    输入: n = 2, prerequisites = [[1,0],[0,1]]
    输出: false
    求任意一个拓扑序 并判断拓扑序含节点数 == 全部节点数
    digraph中 adjacency list 每个节点: set(该节点经某edge指向的节点)
    https://stackoverflow.com/questions/54975278/adjacency-list-representation-in-topological-sort
        @param num_courses: a total of n courses
        @param prerequisites: a list of prerequisite pairs
        @return: true if can finish all courses or false
    """

    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(num_courses)]  # adjacency list
        in_degree = [0] * num_courses
        for (
            to_node,
            from_node,
        ) in (
            prerequisites
        ):  # TODO build graph from edges given 需要注意的是这里的邻接表 根据incoming edges/outgoing edges皆可 并不妨碍解题
            graph[from_node].append(to_node)  # to node 加到from node的adjacency list中
            in_degree[to_node] += 1
        num_chosen = 0  # standard toposort
        q = collections.deque([i for i in range(num_courses) if in_degree[i] == 0])
        while q:
            course_no = q.popleft()
            num_chosen += 1
            # order.append(course_no)  # 这题不需要拓扑序列 只需要知道拓扑序含节点数 == 全部节点数
            for next_course in graph[course_no]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    q.append(next_course)
        return num_chosen == num_courses
