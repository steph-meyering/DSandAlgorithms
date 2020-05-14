// 120. Triangle

/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function (triangle) {
  if (triangle.length === 1) return triangle[0][0];
  let min = Infinity;
  for (let i = 1; i < triangle.length; i++) {
    for (let j = 0; j <= i; j++) {
      if (j === 0) {
        triangle[i][j] = triangle[i][j] + triangle[i - 1][j];
      } else if (j === i) {
        triangle[i][j] = triangle[i][j] + triangle[i - 1][i - 1];
      } else {
        triangle[i][j] =
          triangle[i][j] + Math.min(triangle[i - 1][j], triangle[i - 1][j - 1]);
      }
      if (i === triangle.length - 1) {
        min = Math.min(min, triangle[i][j]);
      }
    }
  }
  return min;
};
