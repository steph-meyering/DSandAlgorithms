// 38. Count and Say

/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    if (n === 1) return "1";
    let ans = ""
    let prevAns = countAndSay(n-1);
    let prevNum = prevAns[0];
    let count = 1;
    for (let i = 1; i < prevAns.length; i++) {
        let curNum = prevAns[i]
        if ( curNum === prevNum) {
            count++;
        } else {
            ans = ans.concat(count, prevNum);
            prevNum = curNum;
            count = 1;
        }
    }
    ans = ans.concat(count, prevNum);
    return ans
};