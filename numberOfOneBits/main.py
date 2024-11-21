class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            res += (n & 1)
            n= n //2
        return res

if __name__ == '__main__':
    so = Solution()
    print(so.hammingWeight(11) == 3)
    print(so.hammingWeight(2147483645) == 30)