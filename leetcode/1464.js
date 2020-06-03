/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
  let max1 = nums[0];
  let idx1 = 0;
  let max2 = nums[nums.length - 1];
  let idx2 = nums.length - 1;
  let j = nums.length - 1;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] >= max1 && i !== idx2) {
      max1 = nums[i];
      idx1 = i;
    }
    if (nums[j] > max2 && j !== idx1) {
      max2 = nums[j];
      idx2 = j;
    }
    j--;
  }
  console.log(max1, max2);
  return (max1 - 1) * (max2 - 1);
};
