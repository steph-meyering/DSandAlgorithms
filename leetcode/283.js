/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
  if (nums.length <= 1) return nums;
  let i = 0;
  for (let j = 1; j < nums.length; j++) {
    if (nums[i] === 0 && nums[j] !== 0) {
      [nums[i], nums[j]] = [nums[j], nums[i]];
      i++;
    } else if (nums[i] !== 0) {
      i++;
    }
  }
};
