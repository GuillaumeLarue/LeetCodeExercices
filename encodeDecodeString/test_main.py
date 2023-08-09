
class TestEncodeDecodeString:

    def test_one(self):
        so = Solution()
        l = ["eee", "eae"]
        res_enc = so.encode(l)
        res_dec = so.decode(res_enc)

        assert res_dec == l

    def test_two(self):
        so = Solution()
        l = ["aera;a;", "ara;araerar"]
        res_enc = so.encode(l)
        res_dec = so.decode(res_enc)

        assert res_dec == l


    def test_three(self):
        so = Solution()
        l = ["", ""]
        res_enc = so.encode(l)
        res_dec = so.decode(res_enc)

        assert res_dec == l

