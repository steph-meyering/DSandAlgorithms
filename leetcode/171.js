// 171. Excel Sheet Column Number

/**
 * @param {string} s
 * @return {number}
 */
var titleToNumber = function (s) {
  s = s.toLowerCase();
  let hash = {};
  let alpha = "abcdefghijklmnopqrstuvwxyz"
    .split("")
    .forEach((char, i) => (hash[char] = i + 1));
  let total = 0;
  for (let i = 0; i < s.length; i++) {
    total += hash[s[i]] * 26 ** (s.length - i - 1);
  }
  return total;
};
