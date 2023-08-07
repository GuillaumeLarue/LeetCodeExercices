from isValidSudoku.main import Solution


class TestIsValidSudoku:
    value = 0

    def test_one(self):
        so = Solution()
        board = [["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
        self.value = so.isValidSudoku(board = board)
        assert self.value == True

    def test_two(self):
        so = Solution()
        board = [["8","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
        self.value = so.isValidSudoku(board = board)
        assert self.value == True

class TestIsValidSudoku:
    def test_valid_h_line(self):
        l = ["8","3",".",".","7",".",".",".","."]
        assert verifHorLine(line = l)
    
    def test_valid_h_line_2(self):
        l = ["8","3",".",".","7",".",".",".","8"]
        assert not verifHorLine(line = l)
    
    def test_valid_h_line_3(self):
        l = [".",".",".",".",".",".",".",".","."]
        assert verifHorLine(line = l)

    def test_valid_v_line(self):
        verifVerLine(board, 8)
        assert True

    def test_valid_v_line_2(self):
        verifVerLine(board, 2)
        assert True
    
    def test_valid_v_line_3(self):
        verifVerLine(board, 1)
        assert True
    
    def test_valid_block(self):
        verifBlock(board, 0,0)
        assert True
    
    def test_valid_block_2(self):
        verifBlock(board, 0,0)
        assert True
    
    def test_valid_block_3(self):
        verifBlock(board, 0,0)
        assert True
