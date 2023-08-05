class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        lis = [0]*26
        lit = [0]*26
        if ls != lt:
            return False
        for e in s:
            lis[ord(e) - ord('a')] += 1
        for e in t:
            lit[ord(e) - ord('a')] += 1
        return lis == lit