// 746. Min Cost Climbing Stairs

/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function (cost) {
  let total = new Array(cost.length + 1).fill(Infinity);
  total[0] = 0;
  total[1] = cost[0];
  for (let i = 1; i < total.length; i++) {
    if (i > 1) {
      total[i] = cost[i - 1] + Math.min(total[i - 1], total[i - 2]);
    }
  }
  return Math.min(total[total.length - 1], total[total.length - 2]);
};
