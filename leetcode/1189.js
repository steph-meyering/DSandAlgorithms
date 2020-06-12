/**
 * @param {string} text
 * @return {number}
 */
var maxNumberOfBalloons = function (text) {
  let hash = {
    b: 0,
    a: 0,
    l: 0,
    o: 0,
    n: 0,
  };
  let min = Infinity;
  for (let i = 0; i < text.length; i++) {
    let char = text[i];
    if (char in hash) {
      hash[char]++;
    }
  }
  console.log(hash);
  hash["l"] = Math.floor(hash["l"] / 2);
  hash["o"] = Math.floor(hash["o"] / 2);
  Object.values(hash).forEach((el) => {
    min = Math.min(el, min);
  });
  console.log(hash);
  return min;
};
