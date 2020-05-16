// 53. Maximum Subarray

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    // initialize array of length nums + 1
    // runningMax = -Infinity
    // iterate over og input
    // Math.max(curnum + preceding one, curnum)

    let max = nums[0];
    let total = new Array(nums.length).fill(nums[0])
    total[0] = nums[0];
    for ( let i = 1; i < nums.length; i++) {
        let curNum = nums[i];
        total[i] = Math.max(curNum, curNum + total[i-1])
        if (total[i] > max) {
            max =  total[i];
        }
    }
    return max;
};