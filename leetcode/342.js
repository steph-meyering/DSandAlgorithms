/**
 * @param {number} num
 * @return {boolean}
 */
var isPowerOfFour = function (num) {
  let square = 1;
  while (square <= num) {
    if (square === Math.abs(num)) return true;
    square = square * 4;
  }
  return false;
};
