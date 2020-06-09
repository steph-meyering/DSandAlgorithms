/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
  if (numRows < 2) return s;
  let res = [];
  for (let i = 0; i < numRows; i++) {
    res.push(new Array());
  }
  let j = 0;
  while (j < s.length) {
    for (let i = 0; i < numRows - 1 && j < s.length; i++) {
      res[i].push(s[j]);
      j++;
    }
    for (let i = numRows - 1; i > 0 && j < s.length; i--) {
      res[i].push(s[j]);
      j++;
    }
  }
  let flatRes = res.reduce((prev, curr) => prev.concat(curr));
  let strRes = "";
  for (char of flatRes) {
    strRes += char;
  }
  return strRes;
};
