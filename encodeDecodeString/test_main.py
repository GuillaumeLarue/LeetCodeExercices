from encodeDecodeString.main import Solution


class TestEncodeDecodeString:
    """
    Input: ["lint","code","love","you"]
    Output: ["lint","code","love","you"]
    Explanation:
    One possible encode method is: "lint:;code:;love:;you"
  
    Input: ["we", "say", ":", "yes"]
    Output: ["we", "say", ":", "yes"]
    Explanation:
    One possible encode method is: "we:;say:;:::;yes"
    """

    def test_one(self):
        so = Solution()
        l = ["eee", "eae"]
        res_enc = so.encode(l)
        assert res_enc == "3#eee3#eae"
        res_dec = so.decode(res_enc)
        # ["eee", "eae"]

        assert res_dec == l

    def test_two(self):
        so = Solution()
        l = ["aeraa;", "ara;araerar"]
        res_enc = so.encode(l)
        # "6#aeraa;11#ara;araerar"
        res_dec = so.decode(res_enc)
        # ["aeraa;", "ara;araerar"]

        assert res_dec == l

    def test_three(self):
        so = Solution()
        l = ["", ""]
        res_enc = so.encode(l)
        # "0#0#"
        res_dec = so.decode(res_enc)
        # ["", ""]

        assert res_dec == l

    def test_four(self):
        so = Solution()
        l = ["aera#a;", "ara#araear"]
        res_enc = so.encode(l)
        # "7#aera#a;10#ara#araear"
        res_dec = so.decode(res_enc)
        # ["aera#a;", "ara#araear"]

        assert res_dec == l
