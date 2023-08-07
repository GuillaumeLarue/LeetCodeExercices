from typing import List


def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_sort = strs.copy()
        for i in range(len(strs_sort)):
            strs_sort[i] = sorted(strs_sort[i])
        l = len(strs)
        res = []
        seeen = [False] * l
        for i in range(l):
            res_tmp = []
            if not seeen[i]:
                res_tmp.append(strs[i])
            else:
                continue
            for j in range(i + 1, l):
                if seeen[j]:
                    continue
                elif strs_sort[i] == strs_sort[j]:
                    res_tmp.append(strs[j])
                    seeen[j] = True
                else:
                    continue
            seeen[i] = True
            if res_tmp != []:
                res.append(res_tmp)
        return res

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        l = len(strs)
        res = []
        seeen = [False] * l
        for i in range(l):
            res_tmp = []
            if not seeen[i]:
                res_tmp.append(strs[i])
            else:
                continue
            for j in range(i + 1, l):
                if seeen[j]:
                    continue
                elif isAnagram(strs[i], strs[j]):
                    res_tmp.append(strs[j])
                    seeen[j] = True
                else:
                    continue
            seeen[i] = True
            if res_tmp != []:
                res.append(res_tmp)
        return res
