class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(31):
            res = (res + (1 & n)) << 1
            n = n >> 1
        res = res + (1 & n)
        return res


if __name__ == '__main__':
    so = Solution()
    print(so.reverseBits(0b11111111111111111111111111111101) == 0b10111111111111111111111111111111)
    print(so.reverseBits(0b00000010100101000001111010011100) == 0b00111001011110000010100101000000)
