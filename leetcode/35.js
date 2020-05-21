// 35. Search Insert Position

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function (nums, target) {
  return bsearch(nums, target, 0, nums.length - 1);
};

function bsearch(nums, target, start, end) {
  let mid = Math.floor(nums.length / 2);
  let left = nums.slice(0, mid);
  let right = nums.slice(mid + 1);
  if (start > end) return start;
  if (nums[mid] === target) {
    return mid;
  } else if (nums[mid] > target) {
    return searchInsert(left, target, 0, left.length - 1);
  } else {
    return searchInsert(right, target, mid, right.length - 1) + mid + 1;
  }
}
