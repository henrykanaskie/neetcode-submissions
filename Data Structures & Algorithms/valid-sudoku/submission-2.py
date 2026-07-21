class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        COLS, ROWS = len(board), len(board[0])

        square = defaultdict(list)
        column = defaultdict(list)
        row = defaultdict(list)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in row[r] or board[r][c] in column[c] or board[r][c] in square[(r//3), (c//3)]:
                    return False
                elif board[r][c] != ".":
                    column[c].append(board[r][c])
                    row[r].append(board[r][c])
                    square[(r//3), (c//3)].append(board[r][c])

        return True
                
                