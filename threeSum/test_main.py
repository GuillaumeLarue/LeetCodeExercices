from threeSum.main import Solution


def equalItems(res, res2):
    if len(res) != len(res2):
        return False
    res = sorted(res)
    res2 = sorted(res2)
    for i in range(len(res)):
        if sorted(res[i]) != sorted(res2[i]):
            return False
    return True


class TestThreeSum:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.threeSum(nums=[-1, 0, 1, 2, -1, -4])
        res = [[-1, -1, 2], [-1, 0, 1]]
        assert self.value == res
        assert equalItems(res, self.value)

    def test_two(self):
        so = Solution()
        self.value = so.threeSum([0, 1, 1])
        res = []
        assert equalItems(res, self.value)

    def test_three(self):
        so = Solution()
        res = [[-9, 0, 9], [-8, -1, 9], [-11, 2, 9], [-6, -3, 9], [-10, 1, 9], [-13, 4, 9], [-12, 3, 9], [-5, -4, 9],
               [-14, 5, 9], [-7, -2, 9], [-15, 6, 9], [-14, 0, 14], [-8, -6, 14], [-11, -3, 14], [-15, 1, 14],
               [-13, -1, 14], [-10, -4, 14], [-9, -5, 14], [-7, -7, 14], [-12, -2, 14], [-8, 0, 8], [-10, 0, 10],
               [0, 0, 0], [-2, 0, 2], [-13, 0, 13], [-3, 0, 3], [-1, 0, 1], [-4, 0, 4], [-11, 0, 11], [-6, 0, 6],
               [-5, 0, 5], [-7, 0, 7], [-8, -2, 10], [-8, 2, 6], [-8, -5, 13], [-8, -3, 11], [-8, 1, 7], [-8, 4, 4],
               [-8, 3, 5], [-12, 2, 10], [-7, -3, 10], [-11, 1, 10], [-13, 3, 10], [-14, 4, 10], [-6, -4, 10],
               [-15, 5, 10], [-9, -1, 10], [-5, -5, 10], [-15, 2, 13], [-3, 1, 2], [-13, 2, 11], [-6, 2, 4], [-5, 2, 3],
               [-10, 2, 8], [-4, 2, 2], [-7, 2, 5], [-9, 2, 7], [-1, -1, 2], [-10, -3, 13], [-14, 1, 13], [-11, -2, 13],
               [-9, -4, 13], [-7, -6, 13], [-12, -1, 13], [-3, -1, 4], [-3, -3, 6], [-5, -3, 8], [-4, -3, 7],
               [-3, -2, 5], [-5, 1, 4], [-4, 1, 3], [-9, 1, 8], [-6, 1, 5], [-7, 1, 6], [-12, 1, 11], [-2, 1, 1],
               [-13, 5, 8], [-13, 6, 7], [-7, 3, 4], [-11, 4, 7], [-12, 4, 8], [-9, 4, 5], [-10, 4, 6], [-15, 4, 11],
               [-2, -2, 4], [-11, 3, 8], [-6, 3, 3], [-10, 3, 7], [-14, 3, 11], [-9, 3, 6], [-2, -1, 3], [-11, 5, 6],
               [-4, -4, 8], [-6, -2, 8], [-14, 6, 8], [-7, -1, 8], [-15, 7, 8], [-4, -1, 5], [-7, -4, 11], [-4, -2, 6],
               [-6, -5, 11], [-6, -1, 7], [-10, 5, 5], [-12, 5, 7], [-10, -1, 11], [-14, 7, 7], [-9, -2, 11],
               [-5, -2, 7], [-5, -1, 6]]
        self.value = so.threeSum(
            [9, 14, 0, -8, 10, 0, 2, 9, -8, 13, -3, 1, 10, -13, 4, 3, -3, -11, 8, -13, -4, -6, 5, -10, -14, 0, 3, -9,
             -9, -7, -11, 8, -8, -4, -15, 9, 11, 3, 3, -11, -7, 7, 5, -12, 1, -14, -1, 13, -9, -8, 7, 2, -6, -11, -1,
             -5, -4, -13, -7, 2, -13, -2, -5, -6, 9, -12, 10, -2, -2, -10, 2, 6, 4, 14, 2, -10, -15, -14, 10, -9, -15,
             -6, 0, -6, -2, 14, -3, 9, 8, -3, -12, 10, 2, -9, 11, -3, -6, -2, 10, 7, 3, -11, -10, -8, -12, -1])
        # assert self.value == res
        assert equalItems(res, self.value)

    def test_four(self):
        so = Solution()
        self.value = so.threeSum([0, 0, 0, 0])
        res = [[0, 0, 0]]
        assert equalItems(res, self.value)
