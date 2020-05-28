/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  //     area = Math.min(a, b) * (j - i)
  let max = 0;
  let i = 0;
  let j = height.length - 1;
  while (i < j) {
    max = Math.max(max, Math.min(height[i], height[j]) * (j - i));
    if (height[i] > height[j]) {
      j--;
    } else {
      i++;
    }
  }
  return max;
};
