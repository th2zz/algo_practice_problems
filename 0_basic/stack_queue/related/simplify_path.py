class Solution:  # https://leetcode.cn/problems/simplify-path/submissions/567166028/?envType=study-plan-v2&envId=top-interview-150
    def simplifyPath(self, path: str) -> str:
        # translate an absolute unix path that contains .. and . to a simplfied path
        # in file system tree we use stack to keep track of current real path (state)
        # think of it like DFS path (dfs use stack, bfs use queue)
        names = path.split("/")
        stack = []
        for name in names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != ".":
                stack.append(name)
        return "/" + "/".join(stack)
