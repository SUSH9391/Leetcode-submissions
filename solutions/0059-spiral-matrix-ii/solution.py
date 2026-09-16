class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        left, right = 0 , n-1
        top, bottom = 0, n-1
        val = 1
        while left<=right:
            #fill row in top row
            for c in range(left,right+1):
                matrix[top][c] = val
                val += 1
            top += 1
            #fill values in the right col
            for r in range(top, bottom+1):
                matrix[r][right] = val
                val+=1
            right -= 1
            # fill values in the bottom row(reverse order)
            for c in range(right,left-1,-1):
                matrix[bottom][c] = val
                val+=1
            bottom -= 1
            #fill values in the left col(reverse order)
            for r in range(bottom,top-1, -1):
                matrix[r][left] = val
                val+=1
            left += 1
        return matrix

