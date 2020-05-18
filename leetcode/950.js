// 950. Reveal Cards In Increasing Order

/**
 * @param {number[]} deck
 * @return {number[]}
 */
const deckRevealedIncreasing = (deck) => {
  deck.sort((a, b) => a - b);
  const ans = [];
  while (deck.length) {
    ans.unshift(deck.pop());
    ans.unshift(ans.pop());
  }
  ans.push(ans.shift());
  return ans;
};
