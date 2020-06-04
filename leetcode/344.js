/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function (s) {
  let j = s.length - 1;
  for (let i = 0; i < j; i++) {
    [s[i], s[j]] = [s[j], s[i]];
    j--;
  }
  return s;
};