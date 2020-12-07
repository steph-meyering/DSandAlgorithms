class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0 for i in range(n)] for i in range(n)]
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        dir_idx = 0
        x, y, val = 0, 0, 1
        while True:
            mat[x][y] = val
            val += 1
            if not self.validPos(x, y, directions[dir_idx], n, mat):
                dir_idx = (dir_idx + 1) % 4
                if not self.validPos(x, y, directions[dir_idx], n, mat):
                    return mat
            dx, dy = directions[dir_idx]
            x += dx
            y += dy
        return mat
                
    
    def validPos(self, x, y, direction, n, matrix):
        dx, dy = direction
        dx += x
        dy += y
        return (0 <= dx < n and 0 <= dy < n and matrix[dx][dy] == 0)
            
            