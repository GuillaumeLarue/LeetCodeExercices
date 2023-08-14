from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        l = len(tokens)
        i = 0
        while i < l:
            if tokens[i].lstrip("-").isnumeric():
                stack.append(tokens[i])
            else:
                a = int(float(stack.pop()))
                b = int(float(stack.pop()))
                if tokens[i] == '+':
                    c = a + b
                elif tokens[i] == '-':
                    c = b - a
                elif tokens[i] == '*':
                    c = a * b
                elif tokens[i] == '/':
                    c = b / a
                stack.append(str(c))
            i += 1
        return int(float(stack.pop()))
