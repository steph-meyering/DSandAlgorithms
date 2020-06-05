/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function (n, memo = {}) {
  if (n === 0) return 0;
  if (n === 1 || n === 2) return 1;
  if (memo[n]) return memo[n];
  memo[n] =
    tribonacci(n - 1, memo) + tribonacci(n - 2, memo) + tribonacci(n - 3, memo);
  return memo[n];
};

const tribonacci = function (n) {
  let res = new Array(n + 1);
  res[0] = 0;
  res[1] = 1;
  res[2] = 1;
  for (let i = 3; i < res.length; i++) {
    res[i] = res[i - 1] + res[i - 2] + res[i - 3];
  }
  return res[n];
};
