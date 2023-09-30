from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ""
        sep = ":;"
        for e in strs:
            s += e
            s += sep

        return s

    def decode(self, strs: str) -> List[str]:
        sep = ":;"
        res = []
        word_tmp = ""
        i = 0
        while (i < len(strs) - 1):
            if strs[i] == sep[0] and strs[i + 1] == sep[1]:
                res.append(word_tmp)
                word_tmp = ""
                i += 1
            else:
                word_tmp += strs[i]
            i += 1

        return res
