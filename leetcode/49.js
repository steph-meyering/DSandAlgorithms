/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  // sort each word's letters, and store original index {sorted word: [idx]}
  // create output array, either push new array, or add to existing
  let strsDup = [...strs];
  let h = {};
  for (let i = 0; i < strs.length; i++) {
    let sortedWord = strsDup[i].split("").sort().join("");
    if (h[sortedWord]) {
      h[sortedWord].push(i);
    } else {
      h[sortedWord] = [i];
    }
  }
  let output = [];
  for (k in h) {
    let sub = [];
    for (let i = 0; i < h[k].length; i++) {
      sub.push(strs[h[k][i]]);
    }
    output.push(sub);
  }
  return output;
};

// Input: ["eat", "tea", "tan", "ate", "nat", "bat"],

// {'aet': [0,1,3],
// 'ant': [2,4],
// 'abt': [1]}
