class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        layers = min(rows,cols) // 2
        for layer in range(layers):
            elements = []
            top, left = layer, layer
            bottom, right = rows - layer - 1,cols - layer - 1
            for c in range(left, right + 1):
                elements.append(grid[top][c])
            for r in range(top +1, bottom):
                elements.append(grid[r][right])
            for c in range(right, left-1, -1):
                elements.append(grid[bottom][c])
            for r in range(bottom - 1, top, -1):
                elements.append(grid[r][left])
            k_mod = k%len(elements)
            rotated = elements[k_mod:] + elements[:k_mod]

            idx = 0
            for c in range(left, right + 1):
                grid[top][c] = rotated[idx]
                idx += 1

            # right column
            for r in range(top + 1, bottom):
                grid[r][right] = rotated[idx]
                idx += 1

            # bottom row
            for c in range(right, left - 1, -1):
                grid[bottom][c] = rotated[idx]
                idx += 1

            # left column
            for r in range(bottom - 1, top, -1):
                grid[r][left] = rotated[idx]
                idx += 1

        return grid
