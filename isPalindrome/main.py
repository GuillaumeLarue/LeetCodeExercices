from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s)-1
        while i < j:
            ci = s[i]
            cj = s[j]
            print(ci, cj)
            if not ((ord(ci) <= ord('z') and ord(ci) >= ord('a')) or (ord(ci) <= ord('9') and ord(ci) >= ord('0'))):
                i += 1
            elif  not ((ord(cj) <= ord('z') and ord(cj) >= ord('a')) or (ord(cj) <= ord('9') and ord(cj) >= ord('0'))):
                j -= 1
            else:
                if ci != cj:
                    return False
                i += 1
                j-=1
        return True