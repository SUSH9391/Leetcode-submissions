class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        m = len(board[0])

        dp = [[[-1, 0] for _ in range(m)] for _ in range(n)]
        dp[-1][-1] = [0,1]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if board[i][j] == "S" : continue
                if board[i][j] == "X" : continue
                if board[i][j] == 'E' : num =0
                else:
                    num = int(board[i][j])
                best =-1
                ncount = 0
                for ni, nj in((i+ 1, j), (i, j+1), (i+1, j+1)):
                    if ni >= n or nj >= m :continue
                    score, count = dp[ni][nj]
                    if score == -1: continue
                    if score > best:
                        best = score
                        ncount = count
                    elif score == best:
                        ncount = (ncount + count) % MOD
                if best != -1: dp[i][j] = [best + num, ncount]
        return dp[0][0] if dp[0][0][0] != -1 else [0, 0]
