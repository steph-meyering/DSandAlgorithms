/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function (nums) {
  let zeroPointer = 0;
  let twoPointer = nums.length - 1;
  let i = 0;
  while (i <= twoPointer) {
    if (nums[i] === 0) {
      [nums[i], nums[zeroPointer]] = [nums[zeroPointer], nums[i]];
      zeroPointer++;
      i++;
    } else if (nums[i] === 2) {
      [nums[i], nums[twoPointer]] = [nums[twoPointer], nums[i]];
      twoPointer--;
    } else {
      i++;
    }
  }
};
