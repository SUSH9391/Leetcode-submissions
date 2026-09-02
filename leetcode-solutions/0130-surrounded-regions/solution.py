class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
            
        ROWS, COLS = len(board), len(board[0])
        
        def capture(r, c):
            # Base case: out of bounds or not an 'O'
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != 'O':
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c - 1)
            capture(r, c + 1)
            
        # 1. Un-indent these loops so they run!
        # Find all 'O's on the border and mark connected 'O's as "T" (Temporary)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r, c)
                    
        # 2. Convert all remaining trapped 'O's to 'X'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = "X"
                    
        # 3. Restore border-connected "T"s back to 'O'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = 'O'
