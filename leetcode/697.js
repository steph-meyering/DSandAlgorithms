/**
 * @param {number[]} nums
 * @return {number}
 */
var findShortestSubArray = function (nums) {
  let hash = {};
  for (let i = 0; i < nums.length; i++) {
    let num = nums[i];
    if (!hash[num]) hash[num] = [];
    hash[num].push(i);
  }
  let maxFreq = 0;
  let minLen = Infinity;
  for (let key of Object.keys(hash)) {
    if (hash[key].length > maxFreq) {
      maxFreq = hash[key].length;
      minLen = hash[key][maxFreq - 1] - hash[key][0] + 1;
    } else if (hash[key].length === maxFreq) {
      minLen = Math.min(hash[key][maxFreq - 1] - hash[key][0] + 1, minLen);
    }
  }
  return minLen;
};
