/**
 * @param {number[]} nums
 * @return {number}
 */
var findUnsortedSubarray = function (nums) {
  let start = 0;
  let end = -1;
  let min = Infinity;
  let max = -Infinity;
  let l = 0;
  let r = nums.length - 1;

  while (r >= 0) {
    nums[l] >= max ? (max = nums[l]) : (end = l);
    nums[r] <= min ? (min = nums[r]) : (start = r);
    l++;
    r--;
  }
  return end - start + 1;
};
