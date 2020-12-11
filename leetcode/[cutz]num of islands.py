class Solution:
    row_dir, col_dir = [1, 0, -1, 0], [0, 1, 0, -1]

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        self.visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        self.row_num = len(grid)
        self.col_num = len(grid[0])

        cnt = 0
        for i in range(self.row_num):
            for j in range(self.col_num):
                if grid[i][j] == "1":
                    if self.visited[i][j] == False:
                        cnt += 1
                        self.dfs(grid, (i, j))
        return cnt

    def dfs(self, grid, coord):
        i, j = coord
        self.visited[i][j] = True

        for k in range(4):
            new_i, new_j = i + self.row_dir[k], j + self.col_dir[k]

            if 0 <= new_i < self.row_num and 0 <= new_j < self.col_num:
                if grid[new_i][new_j] == "1":
                    if self.visited[new_i][new_j] == False:
                        self.dfs(grid, (new_i, new_j))