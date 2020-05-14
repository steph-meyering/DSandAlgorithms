// 64. Minimum Path Sum

/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function (grid) {
  let m = grid.length; // num rows
  let n = grid[0].length; // num elements per row
  let total = new Array(m);
  for (let i = 0; i < m; i++) {
    total[i] = new Array(n).fill(Infinity);
  }
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (i > 0 && j > 0) {
        total[i][j] = Math.min(
          grid[i][j] + total[i][j - 1],
          grid[i][j] + total[i - 1][j]
        );
      } else if (i > 0 && j === 0) {
        total[i][j] = grid[i][j] + total[i - 1][j];
      } else if (j > 0 && i === 0) {
        total[i][j] = grid[i][j] + total[i][j - 1];
      } else {
        total[i][j] = grid[i][j];
      }
    }
  }
  console.log(total);
  return total[m - 1][n - 1];
};
