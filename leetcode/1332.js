/**
 * @param {string} s
 * @return {number}
 */
var removePalindromeSub = function (s) {
  if (s.length === 0) return 0;
  let j = s.length - 1;
  for (let i = 0; i < j; i++) {
    if (s[i] !== s[j]) return 2;
    j--;
  }
  return 1;
};
