// 1143. Longest Common Subsequence

/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    let mat = new Array(text1.length + 1)
    for (let col = 0; col < mat.length; col++){
        mat[col] = new Array(text2.length + 1).fill(0)
    }
    for (let i = 1; i < mat.length; i++){
        for (let j = 1; j < mat[0].length; j++) {
            let prev = mat[i-1][j-1]
            if (text1[i-1] === text2[j-1]) prev++
            mat[i][j] = Math.max(mat[i][j-1], mat[i-1][j], prev)
        }
    }
    return mat[mat.length-1][mat[0].length-1]
};