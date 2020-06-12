/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function (s) {
  let count = 0;
  let countSubs = 0;
  for (let i = 0; i < s.length; i++) {
    s[i] === "L" ? count++ : count--;
    // countSubs = (count === 0 ? countSubs + 1 : countSubs)
    count === 0 ? countSubs++ : countSubs;
    // if (count === 0) countSubs++;
  }
  return countSubs;
};
