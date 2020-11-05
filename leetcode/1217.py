class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        freq = Counter(position)
        res = float("inf")
        odds, evens = 0, 0
        for pos in freq:
            if pos % 2 == 0:
                evens += freq[pos]
            else:
                odds += freq[pos]
        for pos in freq.keys():
            if pos % 2 == 0:
                res = min(res, odds - freq[pos])
            else:
                res = min(res, evens - freq[pos])
        return min(odds, evens)
