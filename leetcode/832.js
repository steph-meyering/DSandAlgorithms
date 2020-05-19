// 832. Flipping an Image

/**
 * @param {number[][]} A
 * @return {number[][]}
 */
var flipAndInvertImage = function (A) {
  let output = [];
  for (let i = 0; i < A.length; i++) {
    let row = [];
    for (let j = A[0].length - 1; j >= 0; j--) {
      let el = A[i][j];
      // el = (el === 0 ? 1 : 0);
      el = el ^ 1;
      row.push(el);
    }
    output.push(row);
  }
  return output;
};
