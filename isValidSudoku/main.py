from typing import List


def verifHorLine(line: List[str]) -> bool:
    l = [0] * 9
    for i in range(len(line)):
        if line[i] == ".":
            continue
        number_tmp = int(line[i])
        l[number_tmp - 1] += 1
        if l[number_tmp - 1] >= 2:
            return False
    return True


def verifVerLine(board: List[List[str]], col) -> bool:
    l = [0] * 9
    for i in range(len(board)):
        if board[i][col] == ".":
            continue
        number_tmp = int(board[i][col])
        l[number_tmp - 1] += 1
        if l[number_tmp - 1] >= 2:
            return False
    return True


def verifBlock(board: List[List[str]], x, y) -> bool:
    # 0 <= i <= 2
    # 0 <= j <= 2
    x = x * 3
    y = y * 3
    l = [0] * 9
    for i in range(3):
        for j in range(3):
            if board[i + x][j + y] == ".":
                continue
            number_tmp = int(board[i + x][j + y])
            l[number_tmp - 1] += 1
            if l[number_tmp - 1] >= 2:
                return False
    return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Verify hor line
        for e in board:
            if not verifHorLine(e):
                return False
        for i in range(9):
            if not verifVerLine(board, i):
                return False
        for i in range(3):
            for j in range(3):
                if not verifBlock(board, i,j):
                    return False
        return True
