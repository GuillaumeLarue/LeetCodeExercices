class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"(": ")", "[": "]", "{": "}"}
        for e in s:
            if e == '(' or e == '[' or e == '{':
                stack.append(e)
            elif e == ')' or e == ']' or e == '}':
                if (len(stack) - 1) >= 0 and e == d[stack[len(stack) - 1]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
