// 118. Pascal's Triangle

/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    if (!numRows) return [];
    let output = [[1]];
    for (let i = 1; i < numRows; i++) {
        let newRow = [1];
        if (i >= 2) {
            for (let j = 0; j < i - 1; j++) {
                newRow.push(output[i-1][j] + output[i-1][j+1] )
            }
        }
        newRow.push(1);
        output.push(newRow);
    }
    return output;
};