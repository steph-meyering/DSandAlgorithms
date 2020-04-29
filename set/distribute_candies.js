// 575. Distribute Candies

// First solution O(n) ?

var distributeCandies = function (candies) {
  let uniqueCandies = {}; // store encountered candies
  let numUniqueCandies = 0; // track number of unique candies
  for (let i = 0; i < candies.length; i++) {
    let candy = candies[i];
    if (uniqueCandies[candy] === undefined) { // if candy hasn't been encountered yet ...
      numUniqueCandies++; // ... increase unique candy counter
      uniqueCandies[candy] = true; // add to our object
    }
  }
  // if half of input or more is unique candies, return input size / 2 
  if (numUniqueCandies > candies.length / 2) return candies.length / 2;
  // otherwise return number of unique candies
  return numUniqueCandies;
};

// Optimized solution using Set:
// O(n) space and time complexity

var distributeCandies = function (candies) {
  return Math.min(new Set(candies).size, candies.length / 2);
};