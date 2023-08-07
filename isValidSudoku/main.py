
def verifHorLine(line: List[str]) -> bool:
    l = [0]*9
    for i in len(line):
        l[line[i]- 1] +=1
        if l[line[i]- 1] >= 2:
            return False
    return True

def verifVerLine(board: List[List[str]]) -> bool:
    return True

def verifBlock(board: List[List[str]], i, j) -> bool:
    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return True