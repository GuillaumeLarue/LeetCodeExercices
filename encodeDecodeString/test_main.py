
class TestEncodeDecodeString:

    """
    Input: ["lint","code","love","you"]
    Output: ["lint","code","love","you"]
    Explanation:
    One possible encode method is: "lint:;code:;love:;you"
    """

    """
    Input: ["we", "say", ":", "yes"]
    Output: ["we", "say", ":", "yes"]
    Explanation:
    One possible encode method is: "we:;say:;:::;yes"
    """

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

