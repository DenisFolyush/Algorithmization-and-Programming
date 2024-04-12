class IslandCounter:
    def mark_current_island(self, matrix, x, y, row, col):
        if x < 0 or x >= row or y < 0 or y >= col or matrix[x][y] != '1':
            return

        # Mark as visited
        matrix[x][y] = '2'

        # Recursive calls for all directions
        self.mark_current_island(matrix, x + 1, y, row, col)  # DOWN
        self.mark_current_island(matrix, x + 1, y + 1, row, col)  # R_DOWN
        self.mark_current_island(matrix, x - 1, y - 1, row, col)  # L_TOP
        self.mark_current_island(matrix, x + 1, y - 1, row, col)  # L_DOWN
        self.mark_current_island(matrix, x - 1, y + 1, row, col)  # R_TOP
        self.mark_current_island(matrix, x, y + 1, row, col)  # RIGHT
        self.mark_current_island(matrix, x - 1, y, row, col)  # TOP
        self.mark_current_island(matrix, x, y - 1, row, col)  # LEFT

    def num_islands(self, grid):
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])

        # Iterate for all cells of the array
        no_of_islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.mark_current_island(grid, i, j, rows, cols)
                    no_of_islands += 1

        return no_of_islands
