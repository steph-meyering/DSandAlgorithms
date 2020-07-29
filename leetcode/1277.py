class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    count += matrix[i][j]
                elif matrix[i][j] == 0:
                    continue
                elif matrix[i][j - 1] >= 1 and matrix[i - 1][j - 1] >= 1 and matrix[i - 1][j] >= 1:
                    matrix[i][j] = min(
                        matrix[i][j - 1], matrix[i - 1][j - 1], matrix[i - 1][j]) + 1
                    count += matrix[i][j]
                else:
                    count += 1
        return count
