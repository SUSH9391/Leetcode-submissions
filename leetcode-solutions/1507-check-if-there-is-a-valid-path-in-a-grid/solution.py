class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        west, north, east, south = 0,1,2,3

        towards_west = (0,-1,east)
        towards_north = (-1,0,south)
        towards_east = (0,1,west)
        towards_south = (1,0,north)

        path = [None,
        (towards_east,None,towards_west,None),
        (None,towards_south,None,towards_north),
        (towards_south,None,None,towards_west),
        (None,None,towards_south,towards_east),
        (towards_north,towards_west,None,None),
        (None,towards_east,towards_north,None),
        ]

        n,m = len(grid),len(grid[0]) #n-rows m-column

        for side in west,north,east,south:
            r,c = 0,0
            while 0<=r<n and 0<=c<m :
                if path[grid[r][c]][side] is None:break
                if r == n-1 and c == m-1 : return True # reached end of the grid

                dy,dx,side = path[grid[r][c]][side]
                r,c = r+dy,c+dx
                if r==0 and c ==0: return False
        return False



