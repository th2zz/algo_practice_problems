class Solution:  # https://leetcode.cn/problems/simplify-path/submissions/567166028/?envType=study-plan-v2&envId=top-interview-150
    def simplifyPath(self, path: str) -> str:
        names = path.split("/")
        stack = []
        for name in names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != ".":
                stack.append(name)
        return "/" + "/".join(stack)
