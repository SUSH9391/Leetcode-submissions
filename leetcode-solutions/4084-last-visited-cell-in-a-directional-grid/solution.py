class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        #visited cells hashset
        #we are supposed to start from (0,0) and simultanouly keep track of visited cells untill we move outside the gris or we land on the cell we have visited
        res = grid
        m = len(res) #row
        n = len(res[0]) #cols
        visited = set()
        r,c = 0,0
        while True:
            visited.add((r,c)) # pair(r,c)
            char = res[r][c]
            if char == 'R':
                nr,nc = r, c+1
            elif char == 'L':
                nr,nc = r,c-1
            elif char == 'U':
                nr,nc = r-1,c
            elif char == 'D':
                nr,nc = r+1,c
            else:
                break
            if not (0 <= nr < m and 0<= nc < n) or (nr,nc) in visited:
                break
            r,c = nr,nc
        return [r,c
               ]
