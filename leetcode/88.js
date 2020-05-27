// 88. Merge Sorted Array

/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (nums1, m, nums2, n) {
  let dup = [...nums1];
  let j = 0;
  let k = 0;
  for (let i = 0; i < nums1.length; i++) {
    if (j === m) {
      nums1[i] = nums2[k];
      k++;
    } else if (k === n) {
      nums1[i] = dup[j];
      j++;
    } else {
      if (dup[j] <= nums2[k]) {
        nums1[i] = dup[j];
        j++;
      } else {
        nums1[i] = nums2[k];
        k++;
      }
    }
  }
  return nums1;
};
