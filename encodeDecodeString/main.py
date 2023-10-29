from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ""
        sep = "#"
        for e in strs:
            leng = len(e)
            s += str(leng)
            s += sep
            s += e

        return s

    def decode(self, strs: str) -> List[str]:
        sep = "#"
        res = []
        word_tmp = ""
        i = 0
        nb_tmp = ""
        while i < len(strs):
            if strs[i] != sep[0]:
                nb_tmp += strs[i]
            elif strs[i] == sep[0]:
                i += 1
                len_str = int(nb_tmp)
                for j in range(len_str):
                    word_tmp += strs[i + j]
                i = i + len_str - 1
                nb_tmp = ""
                res.append(word_tmp)
            i += 1
            word_tmp = ""
        return res


if __name__ == '__main__':
    so = Solution()
    print("|" + so.decode("3#eee3#eae") + "|")
