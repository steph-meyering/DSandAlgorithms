/**
 * @param {number} N
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function (N, trust) {
  if (trust.length === 0 && N === 1) return 1;
  if (trust.length === 0) return -1;
  let potentialJudges = {};
  let notJudges = new Set();
  for (let i = 0; i < trust.length; i++) {
    let t = trust[i];
    potentialJudges[t[1]]
      ? potentialJudges[t[1]]++
      : (potentialJudges[t[1]] = 1);
    notJudges.add(t[0]);
  }
  notJudges.forEach((p) => delete potentialJudges[p]);
  let judge = [];
  for (k in potentialJudges) {
    if (potentialJudges[k] === N - 1) judge.push(k);
  }
  return judge.length === 1 ? judge[0] : -1;
};
