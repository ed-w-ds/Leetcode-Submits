lass Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    # O(9^2) O(9^2)
        cols = collections.defaultdict(set) # hashmap [key->column number : value -> set of values in the column]
        rows = collections.defaultdict(set) # hashmap [key->row number : value -> set of values in the row]
        squares = collections.defaultdict(set) # key->(r//3, c//3) values->values in the square
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row] or
                board[row][col] in cols[col] or
                board[row][col] in squares[(row//3, col//3)]):
                    return False

                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(row//3, col//3)].add(board[row][col])

        return True
