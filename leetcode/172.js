/**
 * @param {number} n
 * @return {number}
 */
var trailingZeroes = function (n) {
  while (n % 5 !== 0) {
    n -= 1;
  }
  let count = 0;
  while (0 < n) {
    let tmp = n;
    while (tmp % 5 === 0) {
      count += 1;
      tmp /= 5;
    }
    n -= 5;
  }
  return count;
};
