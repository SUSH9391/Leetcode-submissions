class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if not n:
            return
        col = set()
        positive_diag = set()
        negative_diag = set()
        res = []
        board = [["."] * n for i in range(n)]
        def dfs(r):
            if r == n :
                copy =["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in positive_diag or (r-c) in negative_diag:
                    continue
                col.add(c)
                positive_diag.add(r+c)
                negative_diag.add(r-c)
                board[r][c] = 'Q'

                dfs(r+1)

                col.remove(c)
                positive_diag.remove(r+c)
                negative_diag.remove(r-c)
                board[r][c] = "."
        dfs(0)
        return res
