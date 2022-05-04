class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        r2lmap = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c in r2lmap.keys():  # right parenthese
                if not stack or stack[-1] != r2lmap[c]:
                    return False
                stack.pop()  # pop left parenthese
            else:  # left parenthese
                stack.append(c)
        return len(stack) == 0
