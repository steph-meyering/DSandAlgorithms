/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
  let merged = [];
  intervals.sort((a, b) => a[0] - b[0]);
  if (intervals.length < 2) return intervals;
  let prev = intervals[0];
  for (let i = 1; i < intervals.length; i++) {
    let cur = intervals[i];
    if (cur[0] > prev[1]) {
      merged.push(prev);
      prev = cur;
    } else {
      let start = prev[0];
      let end = Math.max(cur[1], prev[1]);
      prev = [start, end];
    }
  }
  merged.push(prev);
  return merged;
};
