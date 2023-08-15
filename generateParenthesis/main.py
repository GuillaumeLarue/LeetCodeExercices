from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        tot = []

        def rec(res, l, r):
            if l == r and r == n:
                tot.append(res)
                return
            # Maybe use stack instead of string manipulation of res
            if l < n:
                rec(res + "(", l + 1, r)
            if r < l:
                rec(res + ")", l, r + 1)

        rec("", 0, 0)
        return tot
