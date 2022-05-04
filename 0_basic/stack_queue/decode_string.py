
class Solution:  # https://www.youtube.com/watch?v=qB0zZpBJlh8
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""  # 构建括号里面字符串
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()  # [
                k = ""  # 构建倍率k
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)  # 将k个括号里字符串重新入栈 => 展开内部嵌套字符串
        return "".join(stack)  # now all string are recovered, all in stack
