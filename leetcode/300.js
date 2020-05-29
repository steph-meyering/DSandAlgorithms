/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function (nums) {
  if (nums.length < 1) return 0;
  let arr = new Array(nums.length).fill(1);
  for (let i = 1; i < nums.length; i++) {
    for (let j = i - 1; j >= 0; j--) {
      if (nums[j] < nums[i]) {
        arr[i] = Math.max(arr[j] + 1, arr[i]);
      }
    }
  }
  return Math.max(...arr);
};
