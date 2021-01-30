class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        res = 0
        grid = [[0 for _ in range(m)] for _ in range(n)]
        for x, y in indices:
            for i in range(m):
                grid[x][i] += 1
            for j in range(n):
                grid[j][y] += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] % 2 == 1:
                    res += 1
        return res
