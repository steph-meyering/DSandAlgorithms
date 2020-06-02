/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  let count = 0;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] === "1") {
        markIsland(grid, i, j);
        count++;
      }
    }
  }
  return count;
};

// BFS to mark all adjacent land elements
const markIsland = function (grid, i, j) {
  let q = [[i, j]];
  while (q.length !== 0) {
    let el = q.shift();
    let x = el[0];
    let y = el[1];
    if (grid[x][y] === "1") {
      grid[x][y] = -1;
      if (y > 0 && grid[x][y - 1] === "1") {
        q.push([x, y - 1]);
      }
      if (y < grid[0].length - 1 && grid[x][y + 1] === "1") {
        q.push([x, y + 1]);
      }
      if (x > 0 && grid[x - 1][y] === "1") {
        q.push([x - 1, y]);
      }
      if (x < grid.length - 1 && grid[x + 1][y] === "1") {
        q.push([x + 1, y]);
      }
    }
  }
};
